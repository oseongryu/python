#coding:euc-kr
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


def selectTableSearch(_no):
    cur = conn.cursor()
    sql = "SELECT no, name, tel, etc FROM sample WHERE no = %s"
    cur.execute(sql, (str(_no)))

    rows = cur.fetchall()

    for row in rows:
        print(row)
    return rows

def selectTableList():
    cur = conn.cursor()
    sql = "SELECT no, name, tel, etc FROM sample ORDER BY no asc"
    cur.execute(sql)

    rows = cur.fetchall()
    # for row in rows:
    #     print(row)
    return rows

def insertTable(_no, _name, _tel, _etc):
    cur = conn.cursor()
    sql = "INSERT INTO sample (no, name, tel, etc) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (str(_no), _name, _tel, _etc))
    conn.commit()
    # cur.close()
    # conn.close()

def updateTable(_name, _no):
    cur = conn.cursor()
    sql = """UPDATE sample SET name = %s  WHERE no = %s"""
    cur.execute(sql, (_name, str(_no)))
    conn.commit()


def deleteTable(_no):
    cur = conn.cursor()
    sql = """DELETE from sample WHERE no = %s"""
    cur.execute(sql, str(_no))
    conn.commit()

def selectTableCount():
    cur = conn.cursor()
    sql = """SELECT count(*) FROM sample"""
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows[0])
    return rows[0]


form_class = uic.loadUiType("main_ui.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        self.pushButton_2.clicked.connect(self.btn_add_clicked)
        self.pushButton_3.clicked.connect(self.btn_delete_clicked)
        # self.tableWidget.itemDoubleClicked.connect(self.btn_delete_clicked)

        # self.tableWidget.resize(290, 290)
        # self.tableWidget.setRowCount(2)
        # self.tableWidget.setColumnCount(2)


    def setTableWidgetData(self):
        pass
        # self.tableWidget.setItem(0, 0, QTableWidgetItem("(0,0)"))
        # self.tableWidget.setItem(0, 1, QTableWidgetItem("(0,1)"))
        # self.tableWidget.setItem(1, 0, QTableWidgetItem("(1,0)"))
        # self.tableWidget.setItem(1, 1, QTableWidgetItem("(1,1)"))

    # 조회
    def refresh(self):
        rows = selectTableList()
        self.tableWidget.setRowCount(len(rows))
        count  = 0;
        for row in rows:
            # print(row[0], row[1], row[2], row[3])
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(row[3]))
            count += 1

    def btn_clicked(self):

        self.refresh()

    def btn_add_clicked(self):
        QMessageBox.about(self, "message", "추가")
        insertTable(self.lineEdit.text(), self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text())

        self.refresh()

    def btn_delete_clicked(self):
        # QMessageBox.about(self, "message", "삭제")


        aa = self.tableWidget.currentItem()
        print(aa)
        if aa is not None:
            txt = "row={0}, column={1}, content={2}".format(aa.row(), aa.column(), aa.text())
        else:
            txt = "clicked cell = ({0},{1}) ==>None type<==".format(self.table.currentRow(), self.table.currentColumn())

        msg = QMessageBox.information(self, 'cell 내용', txt)


        # aa = self.tableWidget.selectedIndexes()
        # cell = set((idx.row(), idx.column()) for idx in aa)
        # print(cell)
        # txt1 = "selected cells ; {0}".format(cell)
        # msg = QMessageBox.information(self, 'selectedIndexes()...', txt1)

        self.refresh()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()




# insertTable( 10, 'abc', '010-9999-9999','etceee')
# updateTable('bbe',10)
# deleteTable(10)



