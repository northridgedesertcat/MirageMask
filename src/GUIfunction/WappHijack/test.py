import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QPushButton, QWidget,
                               QVBoxLayout, QLabel)


class SubWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("子窗口")
        self.setGeometry(200, 200, 300, 150)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("操作成功！"))
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        self.setGeometry(100, 100, 400, 300)

        btn = QPushButton("打开子窗口", self)
        btn.clicked.connect(self.open_subwindow)
        btn.resize(120, 40)
        btn.move(140, 130)

    def open_subwindow(self):
        self.sub = SubWindow()
        self.sub.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
