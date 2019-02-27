import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql
import sqlite3
import pyperclip
from PIL import ImageGrab
from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

conn = sqlite3.connect("sqlitedb.db")

cur = conn.cursor()
# cur.execute('DROP TABLE IF EXISTS stocks')

# cur.execute\
# ("""
# CREATE TABLE stocks
# (   id text
# , pw text
# , site text
# , log text
# )
# """)
# conn.commit()


form_class = uic.loadUiType("radiobuttion.ui")[0]




class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox.addItem("id")
        self.comboBox.addItem("name")
        self.comboBox.addItem("xpath")
        # self.comboBox.activated[str].connect(self.combo_box_1_changed)

        self.comboBox_2.addItem("id")
        self.comboBox_2.addItem("name")
        self.comboBox_2.addItem("xpath")
        # self.comboBox_2.activated[str].connect(self.combo_box_1_changed)

        self.comboBox_3.addItem("id")
        self.comboBox_3.addItem("name")
        self.comboBox_3.addItem("xpath")
        # self.comboBox_3.activated[str].connect(self.combo_box_1_changed)

        self.pushButton.clicked.connect(self.click_button_start)

        # self.checkBox.setChecked(True)
        # self.checkBox_2.setChecked(True)
        self.checkBox_5.setChecked(True)
        self.checkBox_6.setChecked(True)


        # 테이블에 클릭 이벤트주기
        self.tableWidget.itemClicked.connect(self.btn_table_clicked)

        # self.tableWidget.itemSelectionChanged.connect((self.btn_table_changed))

        # 테이블 수정 불가능하게 변경
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # row 단위로 선택 가능
    # 테이블 클릭
    def btn_table_clicked(self):
        try:
            tw_si = self.tableWidget.selectedIndexes()

            for idx in tw_si:
                pass

            # row의 0번째
            item = self.tableWidget.item(idx.row(), 0)
            if item is not None:
                txt = item.text()
                self.lineEdit.setText(txt)
            else:
                txt = "no data"

            # row의 1번째
            item = self.tableWidget.item(idx.row(), 1)
            if item is not None:
                txt = item.text()
                self.lineEdit_2.setText(txt)
            else:
                txt = "no data"


        except Exception as e:
            print(e)
            print(type(e))

    def click_button_start(self):
        try:

            combo_box_id = self.comboBox.currentText()
            combo_box_pw = self.comboBox_2.currentText()
            combo_box_login_button = self.comboBox_3.currentText()

            plain_text_edit_url = self.plainTextEdit.toPlainText()
            plain_text_edit_id = self.plainTextEdit_2.toPlainText()
            plain_text_edit_pw = self.plainTextEdit_3.toPlainText()
            plain_text_edit_login_button = self.plainTextEdit_4.toPlainText()

            # 디렉토리가 없을 경우 디렉토리 생성
            dirname = './screenshot'
            if not os.path.isdir(dirname):
                os.mkdir(dirname)

            #  사이트주소, 아이디, 패스워드, 로그인버튼 위치값 여부 확인
            if(plain_text_edit_url== ""):
                self.statusbar.showMessage('사이트 주소가 비었음')
                return
            if(plain_text_edit_id== ""):
                self.statusbar.showMessage('아이디경로가 비었음')
                return
            if(plain_text_edit_pw== ""):
                self.statusbar.showMessage('패스워드경로가 비었음')
                return
            if(plain_text_edit_login_button== ""):
                self.statusbar.showMessage('로그인버튼경로가 비었음')
                return
            else :
                self.statusbar.showMessage('')

            options = webdriver.ChromeOptions()

            # 크롬창숨김 체크박스가 있을 경우 숨기는 옵션으로 변경
            if(self.checkBox.isChecked()):
                options.add_argument('headless')
                options.add_argument('window-size=1920x1080')
                options.add_argument("disable-gpu")

                # UserAgent값 변경
                options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

            driver = webdriver.Chrome('C:\\Temp\\chromedriver.exe', chrome_options=options)

            # 3초 대기하기
            driver.implicitly_wait(3)

            # url 읽어들이기
            driver.get(plain_text_edit_url)


            # 시작전 스크린샷이 True일 경우 수행
            if(self.checkBox_5.isChecked()):
                driver.save_screenshot("./screenshot/"+"aaaa" +"_"+"bbbb"+"_1(before).png")

            if(combo_box_id == "id"):
                driver.find_element_by_id(plain_text_edit_id).clear()
                driver.find_element_by_id(plain_text_edit_id).send_keys("ididid")
            elif(combo_box_id == "name"):
                driver.find_element_by_name(plain_text_edit_id).clear()
                driver.find_element_by_name(plain_text_edit_id).send_keys("ididid")
            elif(combo_box_id == "xpath"):
                driver.find_element_by_xpath(plain_text_edit_id).clear()
                driver.find_element_by_xpath(plain_text_edit_id).send_keys("ididid")


            if(combo_box_pw == "id"):
                driver.find_element_by_id(plain_text_edit_pw).clear()
                driver.find_element_by_id(plain_text_edit_pw).send_keys("ididid")
            elif(combo_box_pw == "name"):
                driver.find_element_by_name(plain_text_edit_pw).clear()
                driver.find_element_by_name(plain_text_edit_pw).send_keys("ididid")
            elif(combo_box_pw == "xpath"):
                driver.find_element_by_xpath(plain_text_edit_pw).clear()
                driver.find_element_by_xpath(plain_text_edit_pw).send_keys("ididid")

            # 아이디비번입력후 스크린샷 찍을 경우 수행
            if(self.checkBox_6.isChecked()):
                driver.save_screenshot("./screenshot/"+"aaaa" +"_"+"bbbb"+"_2(after).png")


            if(combo_box_login_button == "id"):
                driver.find_element_by_id(plain_text_edit_login_button).click()
            elif(combo_box_login_button == "name"):
                driver.find_element_by_name(plain_text_edit_login_button).click()
            elif(combo_box_login_button == "xpath"):
                driver.find_element_by_xpath(plain_text_edit_login_button).click()

            #경고창 체크박스가 True일 경우 수행
            if(self.checkBox_2.isChecked()):
                WebDriverWait(driver, 3).until(EC.alert_is_present(),'Timed out waiting for PA creation confirmation popup to appear.')
                alert = driver.switch_to.alert
                print(alert.text)
                alert.accept()
                # print("alert accepted")

        except Exception as e:
            print(e)
            print(type(e))
            self.statusbar.showMessage("[Error]" + str(type(e)))

    def combo_box_1_changed(self,text):
        try:
            msg = self.comboBox.currentText()
            self.statusbar.showMessage(msg + "선택 됨")
        except Exception as e:
            print(e)
            print(type(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()



