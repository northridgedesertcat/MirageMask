from PySide6.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QIcon, QFont, QPainter, QPen, QBrush,QColor
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve


def show_dialog(parent, message):
    dialog = QDialog(parent)
    dialog.setWindowTitle("高端优雅对话框")
    dialog.setWindowIcon(QIcon("files/12.ico"))
    dialog.setWindowFlags(dialog.windowFlags() | Qt.FramelessWindowHint)
    dialog.setAttribute(Qt.WA_TranslucentBackground)

    # 将 RGB 颜色转换为十六进制字符串
    purple_color = "#{:02x}{:02x}{:02x}".format(189, 147, 249)
    black_color = "#{:02x}{:02x}{:02x}".format(33, 37, 43)

    # 设置对话框的样式
    dialog.setStyleSheet(f"""
        QWidget#dialog_container {{
            background-color: {black_color};
            border-radius: 20px;
            border: 2px solid {purple_color};
        }}
        QLabel {{
            color: {purple_color};
            font-family: "Segoe UI", sans-serif;
            font-size: 18px;
        }}
        QPushButton {{
            background-color: {purple_color};
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            font-family: "Segoe UI", sans-serif;
            font-size: 16px;
        }}
        QPushButton:hover {{
            background-color: #b388ff;
        }}
    """)

    # 主容器
    container = QWidget(dialog)
    container.setObjectName("dialog_container")
    main_layout = QVBoxLayout(dialog)
    main_layout.addWidget(container)
    main_layout.setContentsMargins(10, 10, 10, 10)

    dialog_layout = QVBoxLayout(container)

    # 标题部分
    title_layout = QHBoxLayout()
    title_label = QLabel("重要提示")
    title_font = QFont("Segoe UI", 28, QFont.Bold)
    title_label.setFont(title_font)
    title_label.setAlignment(Qt.AlignCenter)
    title_layout.addWidget(title_label)
    close_button = QPushButton("×")
    close_button.setStyleSheet(f"""
        QPushButton {{
            background-color: transparent;
            color: {purple_color};
            font-size: 32px;
            padding: 0;
            border: none;
        }}
        QPushButton:hover {{
            color: white;
        }}
    """)
    close_button.clicked.connect(dialog.close)
    title_layout.addWidget(close_button, alignment=Qt.AlignTop | Qt.AlignRight)
    dialog_layout.addLayout(title_layout)

    # 分隔线
    separator = QLabel()
    separator.setStyleSheet(f"background-color: {purple_color}; height: 2px;")
    dialog_layout.addWidget(separator)

    # 内容标签
    content_label = QLabel(message)
    content_label.setWordWrap(True)
    content_label.setAlignment(Qt.AlignCenter)
    dialog_layout.addWidget(content_label)

    # 装饰元素（自定义绘制的圆形）
    decoration = QLabel()
    decoration.setFixedSize(100, 100)
    decoration.setAlignment(Qt.AlignCenter)
    decoration.paintEvent = lambda event: draw_circle(decoration, purple_color)
    dialog_layout.addWidget(decoration, alignment=Qt.AlignCenter)

    # 按钮布局
    button_layout = QHBoxLayout()
    ok_button = QPushButton("确定")
    ok_button.clicked.connect(dialog.accept)
    button_layout.addWidget(ok_button, alignment=Qt.AlignCenter)
    dialog_layout.addLayout(button_layout)

    # 添加动画效果
    animation = QPropertyAnimation(dialog, b"windowOpacity")
    animation.setDuration(300)
    animation.setStartValue(0.0)
    animation.setEndValue(1.0)
    animation.setEasingCurve(QEasingCurve.InOutQuad)
    animation.start()

    dialog.exec()


def draw_circle(widget, color):
    painter = QPainter(widget)
    painter.setRenderHint(QPainter.Antialiasing)
    pen = QPen(QColor(color), 4)
    painter.setPen(pen)
    brush = QBrush(QColor(color).lighter(150))
    painter.setBrush(brush)
    rect = widget.rect().adjusted(10, 10, -10, -10)
    painter.drawEllipse(rect)
    painter.end()
