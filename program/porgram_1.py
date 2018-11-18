import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql
import sqlite3
import pyperclip
from PIL import ImageGrab


conn = sqlite3.connect(':memory:')
# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='1234',
#     db='korea',
#     charset='utf8'
# )


form_class = uic.loadUiType("radiobuttion.ui")[0]




class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButton.setChecked(True)
        self.radioButton.clicked.connect(self.radioButtonClicked)
        self.radioButton_2.clicked.connect(self.radioButtonClicked)

    def radioButtonClicked(self):

        try:
            msg = ""
            if self.radioButton.isChecked():
                msg = "일봉"
            elif self.radioButton_2.isChecked():
                msg = "주봉"
                options = QFileDialog.Options()
                options |= QFileDialog.DontUseNativeDialog
                fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                          "All Files (*);;Python Files (*.py)", options=options)
            else:
                msg = "월봉"
            self.statusbar.showMessage(msg + "선택 됨")
        except Exception as e:
            print(e)
            print(type(e))

def openFileNameDialog(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                              "All Files (*);;Python Files (*.py)", options=options)
    if fileName:
        print(fileName)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()



