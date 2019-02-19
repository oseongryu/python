# coding:euc-kr
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='korea',
    charset='utf8'
)


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
    cur = conn.cursor()
    sql = "SELECT no, name, tel, etc FROM sample ORDER BY no asc"
    cur.execute(sql)

    rows = cur.fetchall()

    return rows


# table 데이터 추가
def insertTable(_no, _name, _tel, _etc):
    cur = conn.cursor()
    sql = "INSERT INTO sample (no, name, tel, etc) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (str(_no), _name, _tel, _etc))
    conn.commit()


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
        self.pushButton_2.clicked.connect(self.btn_add_clicked)
        self.pushButton_3.clicked.connect(self.btn_modify_clicked)
        self.pushButton_4.clicked.connect(self.btn_delete_clicked)

        # 테이블에 더블클릭 이벤트주기
        self.tableWidget.itemDoubleClicked.connect(self.btn_table_double_clicked)

        # 테이블 수정 불가능하게 변경
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # 조회
    def refresh(self):
        rows = selectTableList()
        self.tableWidget.setRowCount(len(rows))
        count = 0;
        for row in rows:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(row[3]))
            count += 1

    # 테이블 더블클릭
    def btn_table_double_clicked(self):
        try:
            QMessageBox.information(self, "message", "더블클릭")

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

            # row의 0번째 no
            item = self.tableWidget.item(idx.row(), 0)
            if item is not None:
                txt = item.text()
                self.lineEdit.setText(txt)
            else:
                txt = "no data"

            # row의 1번째 name
            item = self.tableWidget.item(idx.row(), 1)
            if item is not None:
                txt = item.text()
                self.lineEdit_2.setText(txt)
            else:
                txt = "no data"

            # row의 2번째 tel
            item = self.tableWidget.item(idx.row(), 2)
            if item is not None:
                txt = item.text()
                self.lineEdit_3.setText(txt)
            else:
                txt = "no data"

            # row의 3번째 etc
            item = self.tableWidget.item(idx.row(), 3)
            if item is not None:
                txt = item.text()
                self.lineEdit_4.setText(txt)
            else:
                txt = "no data"

            self.refresh()
        except Exception as e:
            print(e)
            print(type(e))

    # 조회 버튼
    def btn_clicked(self):
        try:
            QMessageBox.information(self, "message", "조회")
            self.refresh()
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


