# coding:euc-kr
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

tab_list = []

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파이썬 프로그램")
        self.setGeometry(100, 100,700,800)
        self.setCentralWidget(MyTabWidget(self))

        self.dock_1 = QDockWidget(self)
        self.dock_1.setWindowTitle("")
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_1)
        self.dock_1.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.dock_1.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable )
        # self.dock_1.setMinimumSize(200, 600)
        # self.dock_1.close()


        self.tree_01 = QTreeWidget(self)
        self.tree_01.setHeaderLabels(["Name", "Explanation"])
        # self.treeWidget.setHeaderLabels(["메뉴명"])
        self.tree_01.setColumnWidth(0, 150)
        self.tree_01.setColumnWidth(1, 50)

        self.root = self.tree_01.invisibleRootItem()

        item = QTreeWidgetItem()
        item.setText(0, "자동화관리")
        self.root.addChild(item)

        item = QTreeWidgetItem()
        item.setText(0, "실행이력관리")
        self.root.addChild(item)

        # index = self.tabWidget.addTab(LoginDialog(), "Main")

        # self.tree_01.setTabsClosable(0)
        self.dock_1.setWidget(self.tree_01)

        self.show()



class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # 탭 스크린 설정
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300, 200)

        # 탭 추가
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")

        # 첫번째 탭 레이아웃 설정
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.pushButton2 = QPushButton("PyQt5 button")

        self.pushButton3 = QPushButton("PyQt5 button")

        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.layout.addWidget(self.pushButton2)

        self.tab1.layout.addWidget(self.pushButton3)

        self.tab1.setLayout(self.tab1.layout)

        # 그리고 위젯에 탭 추가
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(QPushButton("y"))
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
