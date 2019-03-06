#coding:euc-kr
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui
from PIL import Image
import urllib.request
import os

form_class = uic.loadUiType("./lib/untitled.ui")[0]
form_class_2 = uic.loadUiType("./lib/dialog_1.ui")[0]

class LoginDialog(QDialog, form_class_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MyWindow(QMainWindow, form_class):
    def __init__(self):

        super().__init__()
        self.setupUi(self)


        # 참고 https://opentutorials.org/module/544/20211
        self.treeWidget.setHeaderLabels(["메뉴", "설명"])
        # self.treeWidget.setHeaderLabels(["메뉴명"])
        self.treeWidget.setColumnWidth(0, 150)
        self.treeWidget.setColumnWidth(1, 50)


        # self.treeWidget.clicked.connect(self.menuDoubleClicked)
        self.treeWidget.itemDoubleClicked.connect(self.menuDoubleClicked)

        self.root = self.treeWidget.invisibleRootItem()



        item = QTreeWidgetItem()
        item.setText(0, "자동화관리")
        item.setText(1, "-")
        self.root.addChild(item)

        item = QTreeWidgetItem()
        item.setText(0, "실행이력관리")

        item.setText(1, "-")
        self.root.addChild(item)

        index = self.tabWidget.addTab(LoginDialog(), "Main")


    # https://wikidocs.net/23755
    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_F:
            # self.showFullScreen()
            self.menuDoubleClicked()

        elif e.key() == Qt.Key_N:
            # self.showNormal()
            self.menuDoubleClicked()

    def menuDoubleClicked(self):
        try:
            menu_name = self.treeWidget.currentItem().text(0)


            index =self.tabWidget.addTab(LoginDialog(), menu_name)
            self.tabWidget.setCurrentIndex(index)
            print(index)

            # tab_name = self.tabWidget.tabText()

        except Exception as e:
            print(e)
            print(type(e))
            self.statusbar.showMessage("[Error] "+str(e)+", " + str(type(e)))
            return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()



