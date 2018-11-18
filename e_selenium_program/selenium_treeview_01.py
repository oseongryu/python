from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# ---------------------------------------------------------------------
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(520, 300)
        self.setWindowTitle("Treeview Example")

        self.treeview = QTreeView(self)

        model = QStandardItemModel()
        rootNode = model.invisibleRootItem()
        branch1 = QStandardItem("Branch 1")
        branch1.appendRow([QStandardItem("Child A"), None])
        childnode = QStandardItem("Child B")
        branch1.appendRow([childnode, None])

        branch2 = QStandardItem("Branch 2")
        branch2.appendRow([QStandardItem("Child C"), None])
        branch2.appendRow([QStandardItem("Child D"), None])

        rootNode.appendRow([branch1, None])
        rootNode.appendRow([branch2, None])

        self.treeview.setModel(model)
        self.treeview.setColumnWidth(0, 150)

        self.setCentralWidget(self.treeview)

        self.treeview.setAlternatingRowColors(True)


# ---------------------------------------------------------------------

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())