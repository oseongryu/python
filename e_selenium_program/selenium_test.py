from PyQt5 import QtCore, QtGui, QtWidgets
def fnTest():
    print('test')

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        fnTest()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

import time
import subprocess

def fnOpen():
    print('호출됨')
    time.sleep(10)
    print('새프로그램 호출')
    subprocess.call('python newTest.py', shell=True)

import threading

if __name__ == "__main__":
    import sys
    print('처음')
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    QtCore.QTimer.singleShot(5000, Dialog.close) #millisecond
    Thread = threading.Timer(1, fnOpen)
    Thread.start()

    sys.exit(app.exec_())

    print('야호')