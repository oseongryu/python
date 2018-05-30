#coding:euc-kr
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui
from PIL import Image
import urllib.request
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

form_class = uic.loadUiType("main_ui.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)

        # self.tableWidget = QTableWidget(self)
        # self.tableWidget.resize(290, 290)
        # self.tableWidget.setRowCount(2)
        # self.tableWidget.setColumnCount(2)


    def setTableWidgetData(self):
        self.tableWidget.setItem(0, 0, QTableWidgetItem("(0,0)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("(0,1)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("(1,0)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("(1,1)"))

    def btn_clicked(self):
        # QMessageBox.about(self, "message", "검색완료")

        self.setTableWidgetData()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()