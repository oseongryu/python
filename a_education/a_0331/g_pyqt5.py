import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300,300,300,400)

        btn1 = QPushButton("Button Click", self)
        btn1.move(20,20)
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        QMessageBox.about(self,"message",'clicked')




app = QApplication(sys.argv)
myWindow = MyWindow()
myWindow.show()
app.exec_()