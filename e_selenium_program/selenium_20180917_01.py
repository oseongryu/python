# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 244)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(350, 10, 75, 23))
        self.addBtn.setObjectName("addBtn")
        self.textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.textBox.setGeometry(QtCore.QRect(10, 10, 331, 20))
        self.textBox.setObjectName("textBox")
        self.textList = QtWidgets.QListView(self.centralwidget)
        self.textList.setGeometry(QtCore.QRect(10, 40, 331, 192))
        self.textList.setObjectName("textList")
        self.exitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(350, 40, 75, 191))
        self.exitBtn.setObjectName("exitBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addBtn.setText(_translate("MainWindow", "ADD"))
        self.exitBtn.setText(_translate("MainWindow", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

