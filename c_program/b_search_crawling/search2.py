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

form_class = uic.loadUiType("main_search2.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_search.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        # QMessageBox.about(self, "message", "검색완료")



        page = urlopen("http://kb.or.kr/p/?j=18")
        document = page.read()
        page.close()

        soup = BeautifulSoup(document, 'html5lib')

        questions = soup.find(class_="round-box")
        # questions_list = questions.find_all("p", class_="lpad15")
        print (questions)
        links = []
        links = questions.get('src')

        # http://kb.or.kr/data/staff/staff_1475835454_u4xxPr7LpE.jpg
        # for question in questions_list:
        #     print(question.get_text())
        # print('http://stackoverflow.com' + question.get('href'))




        URL = 'http://kb.or.kr/' + links[3:]

        with urllib.request.urlopen(URL) as url:
            with open('temp.jpg', 'wb') as f:
                f.write(url.read())

        img = QtGui.QPixmap('temp.jpg')
        self.label_user_img.setGeometry(QtCore.QRect(20, 30, 111, 101))
        self.label_user_img.setPixmap(img)

        img2 = QtGui.QPixmap('main_logo.png')
        self.label_logo.setPixmap(img2)

        self.textEdit_mobile.setText(str("010-1234-1234"))
        self.textEdit_email.setText(str("abc@abc.co.kr"))
        self.textEdit_department.setText(str("전산팀"))

        # self.ElectrodeView = ElectrodeView(self)
        # x_interval = LayoutWidth / 6
        # y_interval = LayoutHeight / 6

        page = urlopen("http://kb.or.kr/p/?j=18")
        document = page.read()
        page.close()

        soup = BeautifulSoup(document, 'html5lib')

        questions = soup.find(class_="pad5 lh_140")
        questions_list = questions.find_all("p", class_="lpad15")

        print(questions_list)
        result = """ """
        for question in questions_list:
            self.listWidget.addItem(question.get_text())
            # result += question.get_text() + "\n"
            # self.label_history.setText(str(result))

        # self.label_history.setText(str("abc@abc.co.kr"))

        # self.listWidget.addItem('aaaaaa')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()