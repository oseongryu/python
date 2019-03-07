# coding:euc-kr
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui
from PIL import Image
import urllib.request
import os
from googletrans import Translator


# treeWidget                    https://opentutorials.org/module/544/20211
# treeWidget dynamic checkbox   https://stackoverflow.com/questions/31342228/pyqt-tree-widget-adding-check-boxes-for-dynamic-removal
# keyPressEvent                 https://wikidocs.net/23755
# tabWidget                     https://stackoverflow.com/questions/45828478/how-to-et-current-tab-of-qtabwidget-by-name
#                               https://deptinfo-ensip.univ-poitiers.fr/ENS/pyside-docs/PySide/QtGui/QTabWidget.html

form_class = uic.loadUiType("./lib/untitled.ui")[0]
form_class_2 = uic.loadUiType("./lib/dialog_1.ui")[0]
form_class_3 = uic.loadUiType("./lib/english_dialog.ui")[0]

tab_list = []


class EnglishDialog(QDialog, form_class_3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        translator = Translator()
        print(translator.translate('안녕하세요', src='ko', dest='en').origin)
        print(translator.translate('안녕하세요.', src='ko', dest='en').text)

class LoginDialog(QDialog, form_class_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MyWindow(QMainWindow, form_class):
    def __init__(self):

        super().__init__()
        self.setupUi(self)

        self.treeWidget.setHeaderLabels(["메뉴", "설명"])
        # self.treeWidget.setHeaderLabels(["메뉴명"])
        self.treeWidget.setColumnWidth(0, 150)
        self.treeWidget.setColumnWidth(1, 50)

        # self.treeWidget.clicked.connect(self.menuDoubleClicked)
        self.treeWidget.itemDoubleClicked.connect(self.menuDoubleClicked)

        self.root = self.treeWidget.invisibleRootItem()

        item = QTreeWidgetItem()
        item.setText(0, "자동화관리")
        item.setText(1, "LoginDialog")
        self.root.addChild(item)

        item = QTreeWidgetItem()
        item.setText(0, "실행이력관리")
        item.setText(1, "LoginDialog")
        self.root.addChild(item)
        
        item = QTreeWidgetItem()
        item.setText(0, "영어다이어리")
        item.setText(1, "EnglishDialog")
        self.root.addChild(item)

        index = self.tabWidget.addTab(LoginDialog(), "Main")

        self.tabWidget.setTabsClosable(0)
        self.tabWidget.tabCloseRequested.connect(self.close_handler)

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
            menu_dialog = self.treeWidget.currentItem().text(1) +'()'
            # print(self.treeWidget.currentColumn())
            # tab_name = self.tabWidget.tabText(0)

            result = tab_list.__contains__(menu_name)

            if result != True :
                if menu_name == "자동화관리":
                    tab_list.append(menu_name)
                    index =self.tabWidget.addTab(LoginDialog(), menu_name)
                    self.tabWidget.setCurrentIndex(index)
                    # print(self.tabWidget.tabText(index)+ str(index))
                    print(self.tabWidget.count())
                elif menu_name == "실행이력관리":
                    tab_list.append(menu_name)
                    index =self.tabWidget.addTab(LoginDialog(), menu_name)
                    self.tabWidget.setCurrentIndex(index)
                    # print(self.tabWidget.tabText(index)+ str(index))
                    print(self.tabWidget.count())
                elif menu_name == "영어다이어리":
                    tab_list.append(menu_name)
                    index = self.tabWidget.addTab(EnglishDialog(), menu_name)
                    self.tabWidget.setCurrentIndex(index)
                    # print(self.tabWidget.tabText(index)+ str(index))
                    print(self.tabWidget.count())
            else :
                self.tabWidget.setCurrentIndex(0)


        except Exception as e:
            print(e)
            print(type(e))
            self.statusbar.showMessage("[Error] " + str(e) + ", " + str(type(e)))
            return

    def close_handler(self):
        index = self.tabWidget.currentIndex()
        self.tabWidget.removeTab(index)


    # def search(self):
    #     try:
    #         page = self.tabWidget.findChild(QWidget, "자동화관리")
    #         print(page)
    #
    #     except Exception as e:
    #         print(e)
    #         print(type(e))
    #         self.statusbar.showMessage("[Error] " + str(e) + ", " + str(type(e)))
    #         return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()



