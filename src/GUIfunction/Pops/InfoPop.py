import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                               QVBoxLayout, QHBoxLayout, QGraphicsDropShadowEffect)
from PySide6.QtGui import QColor, QFont
from PySide6.QtCore import Qt, QSize


class MessagePopup(QWidget):
    def __init__(self, message="", parent=None):
        super().__init__(parent)
        # 定义颜色方案
        self.bg_color = QColor(37, 33, 43)  # 主背景
        self.panel_color = QColor(40, 44, 52)  # 面板色
        self.accent_color = QColor(255, 110, 132)  # 强调色
        self.highlight_color = QColor(189, 147, 249)  # 新增高亮色

        self.initUI(message)

    def initUI(self, message):
        # 窗口基础设置
        self.setWindowTitle('系统提示')
        self.setFixedSize(420, 220)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        # 创建阴影效果
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(3, 3)
        self.setGraphicsEffect(shadow)

        # 主布局
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 25, 20, 20)
        main_layout.setSpacing(15)

        # 标题栏
        title = QLabel("🦄 消息提示")
        title.setFont(QFont("Microsoft YaHei", 12, QFont.Bold))

        # 消息内容
        msg_label = QLabel(message)
        msg_label.setFont(QFont("Microsoft YaHei", 10))
        msg_label.setWordWrap(True)
        msg_label.setAlignment(Qt.AlignCenter)

        # 确认按钮
        btn_confirm = QPushButton("确认")
        btn_confirm.setFixedSize(100, 36)
        btn_confirm.clicked.connect(self.close)

        # 按钮布局
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(btn_confirm)
        btn_layout.addStretch()

        # 组合元素
        main_layout.addWidget(title)
        main_layout.addWidget(msg_label)
        main_layout.addStretch()
        main_layout.addLayout(btn_layout)

        # 应用样式
        self.setStyleSheet(f"""
            QWidget {{
                background-color: rgb{self.bg_color.getRgb()[:3]};
                color: rgb{self.highlight_color.getRgb()[:3]};
            }}
            QLabel {{
                color: rgb{self.highlight_color.getRgb()[:3]};
            }}
            QPushButton {{
                background-color: rgb{self.panel_color.getRgb()[:3]};
                border: 1px solid rgb{self.accent_color.getRgb()[:3]};
                border-radius: 8px;
                padding: 8px;
                font: 10pt "Microsoft YaHei";
                min-width: 80px;
                color: white;
            }}
            QPushButton:hover {{
                background-color: rgb{self.accent_color.getRgb()[:3]};
            }}
            QPushButton:pressed {{
                background-color: rgb{self.highlight_color.getRgb()[:3]};
            }}
        """)

        # 设置圆角窗口
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet(self.styleSheet() + f"""
            #MessagePopup {{
                background-color: rgb{self.bg_color.getRgb()[:3]};
                border-radius: 12px;
                border: 1px solid rgb{self.highlight_color.getRgb()[:3]};
            }}
        """)
        self.setObjectName("MessagePopup")

        self.setLayout(main_layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 使用示例
    popup = MessagePopup(
        message="这是一条重要的系统通知内容，可以包含多行文本信息。\n当前系统时间：2024-03-20 14:30"
    )
    popup.show()
    sys.exit(app.exec())
