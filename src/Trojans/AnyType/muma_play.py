import os
import sys
import info_control

class video_play:
    def __init__(self,file):
        self.file=file

    def play_video(self):
        os.startfile(self.file)

    # def write_file(self):
    #     self.path,self.name=info_control.get_curry_path_name()
    #     info_control.copy_file(self.file,self.path+self.name)


if __name__=="__main__":
    v=video_play("files/1.mp4")
    v.write_video()
