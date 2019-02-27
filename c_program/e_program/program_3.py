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
import csv

conn = sqlite3.connect("sqlitedb.db")

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS stocks')

cur.execute\
("""
CREATE TABLE stocks
(   id text
, pw text
)
""")
conn.commit()


form_class = uic.loadUiType("radiobutton.ui")[0]

# table 리스트
def selectTableList():
    cur = conn.cursor()
    sql = "SELECT id, pw FROM stocks"
    cur.execute(sql)

    rows = cur.fetchall()

    return rows

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
        self.pushButton_3.clicked.connect(self.openFileNameDialog)
        self.pushButton_4.clicked.connect(self.loadFile)


        # self.checkBox.setChecked(True)
        # self.checkBox_2.setChecked(True)
        self.checkBox_5.setChecked(True)
        self.checkBox_6.setChecked(True)

        # 테이블 수정 불가능하게 변경
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # row 단위로 선택 가능

        self.lineEdit_5.setDisabled(1)

    def click_button_start(self):
        try:

            combo_box_id = self.comboBox.currentText()
            combo_box_pw = self.comboBox_2.currentText()
            combo_box_login_button = self.comboBox_3.currentText()

            line_edit_url = self.lineEdit.text()
            line_edit_id = self.lineEdit_2.text()
            line_edit_pw = self.lineEdit_3.text()
            line_edit_login_button = self.lineEdit_4.text()

            #  사이트주소, 아이디, 패스워드, 로그인버튼 위치값 여부 확인
            if(line_edit_url== ""):
                self.statusbar.showMessage('사이트 주소가 비었음')
                return
            if(line_edit_id== ""):
                self.statusbar.showMessage('아이디경로가 비었음')
                return
            if(line_edit_pw== ""):
                self.statusbar.showMessage('패스워드경로가 비었음')
                return
            if(line_edit_login_button== ""):
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

            driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)


            # 3초 대기하기
            driver.implicitly_wait(3)

            # url 읽어들이기
            driver.get(line_edit_url)




            # 디렉토리가 없을 경우 디렉토리 생성
            dirname = './screenshot'
            if not os.path.isdir(dirname):
                os.mkdir(dirname)

            rows = selectTableList()
            # print(rows)
            id  = ''
            pw  = ''
            index = ''
            alert_message = ''
            for idx, row in enumerate(rows, 1):
                id = row[0]
                pw = row[1]
                index = str(idx)

                # 시작전 스크린샷이 True일 경우 수행
                if(self.checkBox_5.isChecked()):
                    driver.save_screenshot("./screenshot/"+index+"_1_"+id+"_"+pw+"(before).png")



                if(combo_box_id == "id"):
                    driver.find_element_by_id(line_edit_id).clear()
                    driver.find_element_by_id(line_edit_id).send_keys(id)
                elif(combo_box_id == "name"):
                    driver.find_element_by_name(line_edit_id).clear()
                    driver.find_element_by_name(line_edit_id).send_keys(id)
                elif(combo_box_id == "xpath"):
                    driver.find_element_by_xpath(line_edit_id).clear()
                    driver.find_element_by_xpath(line_edit_id).send_keys(id)

                if(combo_box_pw == "id"):
                    driver.find_element_by_id(line_edit_pw).clear()
                    driver.find_element_by_id(line_edit_pw).send_keys(pw)
                elif(combo_box_pw == "name"):
                    driver.find_element_by_name(line_edit_pw).clear()
                    driver.find_element_by_name(line_edit_pw).send_keys(pw)
                elif(combo_box_pw == "xpath"):
                    driver.find_element_by_xpath(line_edit_pw).clear()
                    driver.find_element_by_xpath(line_edit_pw).send_keys(pw)


                # 아이디비번입력후 스크린샷 찍을 경우 수행
                if(self.checkBox_6.isChecked()):
                    driver.save_screenshot("./screenshot/" + index + "_2_" + id + "_" + pw + "(after).png")


                if(combo_box_login_button == "id"):
                    driver.find_element_by_id(line_edit_login_button).click()
                elif(combo_box_login_button == "name"):
                    driver.find_element_by_name(line_edit_login_button).click()
                elif(combo_box_login_button == "xpath"):
                    driver.find_element_by_xpath(line_edit_login_button).click()


                #경고창 체크박스가 True일 경우 수행
                if(self.checkBox_2.isChecked()):
                    WebDriverWait(driver, 3).until(EC.alert_is_present(),'Timed out waiting for PA creation confirmation popup to appear.')
                    alert = driver.switch_to.alert
                    alert_message = alert.text
                    # print(alert.text)
                    alert.accept()

                    # print("alert accepted")
                now = time.localtime()
                print(index + ' ' + '%04d/%02d/%02d %02d:%02d:%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec) + ' ' + id  +' '+ pw +' ' + alert_message)

                print( )
        except Exception as e:
            print(e)
            print(type(e))
            self.statusbar.showMessage("[Error] "+str(e)+", " + str(type(e)))
            return

    def openFileNameDialog(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            # fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","csv Files (*.csv);;All Files (*)", options=options)
            fileName, _ = QFileDialog.getOpenFileName(self, "csv 파일을 선택하세요.", "","csv Files (*.csv);;All Files (*)", options=options)

            if fileName:
                print(fileName)
                self.lineEdit_5.clear()
                self.lineEdit_5.setText(fileName)
        except Exception as e:
            print(e)
            print(type(e))
            self.statusbar.showMessage("[Error] " + str(e) + ", " + str(type(e)))
            return

    def loadFile(self):
        try:
            line_edit_csv_file_dir = self.lineEdit_5.text().replace(r"\\",r"\\")
            f = open(line_edit_csv_file_dir, 'r')  # open the csv data file
            # next(f, None) # skip the header row
            reader = csv.reader(f)
            for row in reader:
                cur.execute('INSERT INTO  stocks VALUES (?,?)', row)
            conn.commit()

            # for row in cur.execute("SELECT * FROM stocks"):
            #     print(row)
            f.close()

            # conn.close()
            self.pushButton_3.setDisabled(1)
            self.pushButton_4.setDisabled(1)


            # 조회
            rows = selectTableList()
            self.tableWidget.setRowCount(len(rows))
            count = 0;
            # self.lineEdit_3.setText("1")
            # self.lineEdit_4.setText(str(len(rows)))
            # self.pushButton.setDisabled(1)
            for row in rows:
                self.tableWidget.setItem(count, 0, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(count, 1, QTableWidgetItem(row[1]))
                # self.tableWidget.setItem(count, 2, QTableWidgetItem(row[2]))
                # self.tableWidget.setItem(count, 3, QTableWidgetItem(row[3]))
                count += 1
            self.tableWidget.selectRow(0)

        except Exception as e:
            print(e)
            print(type(e))
            self.statusbar.showMessage("[Error] " + str(e) + ", " + str(type(e)))
            return



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()



