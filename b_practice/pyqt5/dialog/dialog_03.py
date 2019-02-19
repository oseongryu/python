import os

# from dump_io import dump_io
# from tb_item_sim_mode import tb_item_sim_mode
# from tb_item_sun import tb_item_sun
#
# from code_ctrl import enable_betafeatures
# from cal_path import get_css_path

# qt
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt, QFile, QIODevice
from PyQt5.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QHBoxLayout, QPushButton, QDialog, QFileDialog, QToolBar, \
    QMessageBox, QLineEdit, QToolButton
from PyQt5.QtWidgets import QTabWidget

# from icon_lib import QIcon_load
#
# from about import about_dlg
#
# from fx_selector import fx_selector
# from tb_optical_model import tb_optical_model
# from tb_spectrum import tb_spectrum
#
# from util import wrap_text


class ribbon_solar(QTabWidget):
    def goto_page(self, page):
        self.blockSignals(True)
        for i in range(0, self.count()):
            if self.tabText(i) == page:
                self.setCurrentIndex(i)
                break
        self.blockSignals(False)

    def optics(self):
        toolbar = QToolBar()
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolbar.setIconSize(QSize(42, 42))

        self.run = QAction(QIcon_load("media-playback-start"), wrap_text(_("Calculate"), 5), self)
        toolbar.addAction(self.run)

        self.export = QAction(QIcon_load("document-export"), wrap_text(_("Export spectrum"), 5), self)
        # self.export.triggered.connect(self.save_image)
        toolbar.addAction(self.export)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        toolbar.addWidget(spacer)

        self.help = QAction(QIcon_load("help"), _("Help"), self)
        toolbar.addAction(self.help)
        return toolbar

    def readStyleSheet(self, fileName):
        css = None
        file = QFile(fileName)
        if file.open(QIODevice.ReadOnly):
            css = file.readAll()
            file.close()
        return css

    def callback_about_dialog(self):
        dlg = about_dlg()
        dlg.exec_()

    def __init__(self):
        QTabWidget.__init__(self)
        self.setMaximumHeight(120)
        # self.setStyleSheet("QWidget {	background-color:cyan; }")

        self.about = QToolButton(self)
        self.about.setText(_("About"))
        self.about.pressed.connect(self.callback_about_dialog)

        self.setCornerWidget(self.about)

        w = self.optics()
        self.addTab(w, _("Spectrum"))

        sheet = self.readStyleSheet(os.path.join(get_css_path(), "style.css"))
        if sheet != None:
            sheet = str(sheet, 'utf-8')
            self.setStyleSheet(sheet)