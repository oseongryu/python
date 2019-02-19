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

lists_id = []
lists_pw = []


#
f_id = open("C:\\Temp\\id.txt", 'r', encoding='utf-8')
while True:
    line_id = f_id.readline()
    if not line_id: break
    # print(line_id)
    lists_id.append(line_id.rstrip().lstrip())
f_id.close()


f_pw = open("C:\\Temp\\pw.txt", 'r', encoding='utf-8')
while True:
    line_pw = f_pw.readline()
    if not line_pw: break
    # print(line_pw)
    lists_pw.append(line_pw.rstrip().lstrip())
f_pw.close()

# for list_id in lists_id:
#     for list_pw in lists_pw:
#         print(list_id,list_pw)


# no로 검색
def selectTableSearch(_no):
    cur = conn.cursor()
    sql = "SELECT no, name, tel, etc FROM sample WHERE no = %s"
    cur.execute(sql, (str(_no)))

    rows = cur.fetchall()

    for row in rows:
        print(row)
    return rows


# table 리스트
def selectTableList():
    # cur = conn.cursor()
    # sql = "SELECT no, name, tel, etc FROM sample ORDER BY no asc"
    # cur.execute(sql)
    #
    # rows = cur.fetchall()
    lists_id_pw =[]
    for list_id in lists_id:
        for list_pw in lists_pw:
            # print(list_id, list_pw)
            lists_id_pw.append([list_id,list_pw])

    return lists_id_pw


# table 데이터 추가
def insertTable(_no, _name, _tel, _etc):
    pyperclip.setcb("abcdedadf")
    spam = pyperclip.getcb()
    # cur = conn.cursor()
    # sql = "INSERT INTO sample (no, name, tel, etc) VALUES (%s, %s, %s, %s)"
    # cur.execute(sql, (str(_no), _name, _tel, _etc))
    # conn.commit()


# table 데이터 수정
def updateTable(_no, _name, _tel, _etc):
    cur = conn.cursor()
    sql = """UPDATE sample SET name = %s , tel = %s, etc = %s WHERE no = %s"""
    cur.execute(sql, (_name, _tel, _etc, str(_no)))
    conn.commit()


# table 데이터 삭제
def deleteTable(_no):
    cur = conn.cursor()
    sql = """DELETE from sample WHERE no = %s"""
    cur.execute(sql, str(_no))
    conn.commit()


form_class = uic.loadUiType("main_ui.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_2.clicked.connect(self.btn_id_paste_clicked)
        self.pushButton_3.clicked.connect(self.btn_pw_paste_clicked)
        self.pushButton_4.clicked.connect(self.btn_next_clicked)
        self.pushButton_5.clicked.connect(self.btn_screen_shot_clicked)

        # 테이블에 클릭 이벤트주기
        self.tableWidget.itemClicked.connect(self.btn_table_clicked)

        self.tableWidget.itemSelectionChanged.connect((self.btn_table_changed))

        # 테이블 수정 불가능하게 변경
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # row 단위로 선택 가능
        self.lineEdit.setDisabled(1)
        self.lineEdit_2.setDisabled(1)
        self.lineEdit_3.setDisabled(1)
        self.lineEdit_4.setDisabled(1)


    # 조회
    def refresh(self):
        rows = selectTableList()
        self.tableWidget.setRowCount(len(rows))
        count = 0;
        self.lineEdit_3.setText("1")
        self.lineEdit_4.setText(str(len(rows)))
        self.pushButton.setDisabled(1)
        for row in rows:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(row[1]))
            # self.tableWidget.setItem(count, 2, QTableWidgetItem(row[2]))
            # self.tableWidget.setItem(count, 3, QTableWidgetItem(row[3]))
            count += 1


    # 테이블 클릭
    def btn_table_clicked(self):
        try:
            # QMessageBox.information(self, "message", "클릭")

            # aa = self.tableWidget.selectedRanges()
            # txt = []
            # for idx, sel in enumerate(aa):
            #     # print(sel.rowCount(), sel.columnCount(), sel.topRow(), sel.leftColumn(), sel.bottomRow(), sel.rightColumn())
            #     tmp = "ranage {0} ; row/col Count={1}/{2} ".format(idx, sel.rowCount(), sel.columnCount()) + \
            #           "({0},{1}) ~ ({2},{3})".format(sel.topRow(), sel.leftColumn(), sel.bottomRow(), sel.rightColumn())
            #     txt.append(tmp)
            # msg = QMessageBox.information(self, 'selectedRanges()...', '\n'.join(txt))

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

            # row의 2번째 tel
            # item = self.tableWidget.item(idx.row(), 2)
            # if item is not None:
            #     txt = item.text()
            #     self.lineEdit_3.setText(txt)
            # else:
            #     txt = "no data"

            # row의 3번째 etc
            # item = self.tableWidget.item(idx.row(), 3)
            # if item is not None:
            #     txt = item.text()
            #     self.lineEdit_4.setText(txt)
            # else:
            #     txt = "no data"

            # self.refresh()
        except Exception as e:
            print(e)
            print(type(e))

    # 테이블체인지 버튼
    def btn_table_changed(self):
        try:
            # QMessageBox.information(self, "message", "조회")
            # self.refresh()
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

    # 조회 버튼
    def btn_clicked(self):
        try:
            # QMessageBox.information(self, "message", "조회")
            self.refresh()
            self.tableWidget.selectRow(0)
        except Exception as e:
            print(e)
            print(type(e))

    # 아이디 복사 버튼
    def btn_id_paste_clicked(self):
        try:
            pyperclip.copy(self.lineEdit.text())
            spam = pyperclip.paste()

            # QMessageBox.information(self, "message", "추가")
            # insertTable(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())

            # self.refresh()
        except Exception as e:
            print(e)
            print(type(e))

    # 패스워드 복사 버튼
    def btn_pw_paste_clicked(self):
        try:
            pyperclip.copy(self.lineEdit_2.text())
            spam = pyperclip.paste()

            # QMessageBox.information(self, "message", "추가")
            # insertTable(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())

            # self.refresh()
        except Exception as e:
            print(e)
            print(type(e))

    # 테이블 다음 버튼
    def btn_next_clicked(self):
        try:
            number = self.tableWidget.currentRow() + 1
            self.lineEdit_3.setText(str(number+1))
            self.tableWidget.selectRow(number)
        except Exception as e:
            print(e)
            print(type(e))

    # 스크린샷 버튼
    def btn_screen_shot_clicked(self):
        try:
            img = ImageGrab.grab()
            img.save("ScreenShot.png")
        except Exception as e:
            print(e)
            print(type(e))

    # 추가 버튼
    def btn_add_clicked(self):
        try:

            QMessageBox.information(self, "message", "추가")
            insertTable(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())

            self.refresh()
        except Exception as e:
            print(e)
            print(type(e))

    # 수정 버튼
    def btn_modify_clicked(self):
        try:
            QMessageBox.information(self, "message", "수정")
            updateTable(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())

            self.refresh()
        except Exception as e:
            print(e)
            print(type(e))

    # 삭제 버튼 (no 위치에 가져다 놓고 삭제를 누르면 실행 됨)
    def btn_delete_clicked(self):

        try:
            QMessageBox.information(self, "message", "삭제")

            ci = self.tableWidget.currentItem()
            # if ci is not None:
            #     txt = "row={0}, column={1}, content={2}".format(ci.row(), ci.column(), ci.text())
            # else:
            #     txt = "clicked cell = ({0},{1}) ==>None type<==".format(self.table.currentRow(), self.table.currentColumn())
            # msg = QMessageBox.information(self, 'cell 내용', txt)

            deleteTable(ci.text())
            self.refresh()

        except Exception as e:
            print(e)
            print(type(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

# updateTable('bbe',10)


