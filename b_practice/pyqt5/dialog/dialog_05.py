import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5 import uic

form_class = uic.loadUiType("main_ui.ui")[0]
# form_class_2 = uic.loadUiType("dialog.ui")[0]
form_class_2 = uic.loadUiType("dialog_2.ui")[0]

load_windows_ui = "main_ui.ui"
load_dialog_ui = "dialog.ui"

class LoginPage(QDialog, form_class_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # loadUi('dialog.ui', self)

class RegisterPage(QDialog):
    def __init__(self):
        super(RegisterPage, self).__init__()
        loadUi('dialog.ui', self)

class HomePage(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.executeLoginPage)

        self.pushButton_2.clicked.connect(self.executeRegisterPage)
        self.pushButton_2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
        self.pushButton_2.setText('Press Me')
        print(self.pushButton_2.text())
        menu = QMenu()
        menuItem1 = menu.addAction('Menu Item1')
        menuItem2 = menu.addAction('Menu Item2')

        self.pushButton_2.setMenu(menu)

    def executeLoginPage(self):
        login_page = LoginPage()
        login_page.pushButton.clicked.connect(self.DialogClicked)

        login_page.pushButton_2.clicked.connect(self.executeRegisterPage)
        login_page.exec_()

        print("b")

    def executeRegisterPage(self):
        register_page = RegisterPage()
        register_page.exec_()

        print("a")
    def DialogClicked(self):
        QMessageBox.information(self, "message", "클릭")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = HomePage()
    widget.show()
    sys.exit(app.exec_())