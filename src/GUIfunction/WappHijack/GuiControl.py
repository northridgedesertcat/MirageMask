'''
    本文件用于WappHijack功能中，Gui页面有关的代码

'''


from PySide6.QtWidgets import QFileDialog


class GuiControl:
    def select_file(self, win):
        # 图形化查找文件路径
        file_path, _ = QFileDialog.getOpenFileName(win, "选择单个文件", "", "应用程序 (*.exe)")
        return file_path

    def set_App(self, win, line):
        FilePath = self.select_file(win)
        line.setText(FilePath)
        self.confs['app']=FilePath

    def set_CS(self, win, line):
        FilePath = self.select_file(win)
        line.setText(FilePath)
        self.confs['CS']=FilePath

