import sys
from PyQt5.QtWidgets import *
class MyTest(QMainWindow):
    def __init__(self):
        super().__init__()
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)
        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)
        btn1.clicked.connect(self.button_clicked)
        btn2.clicked.connect(self.button_clicked)
        self.statusbar = self.statusBar()
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
    def button_clicked(self):
    # 사용자 정의 slot -- @pyqtSlot() decorator 사용하면 가독성 좋을듯.
        sender = self.sender()
        self.statusbar.showMessage(sender.text() + ' was pressed')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyTest()
    sys.exit(app.exec_())

