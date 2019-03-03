from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDateTime


# reference: https://stackoverflow.com/questions/18196799/how-can-i-show-a-pyqt-modal-dialog-and-get-data-out-of-its-controls-once-its-clo
class DateDialog(QDialog):
    def __init__(self, parent = None):
        super(DateDialog, self).__init__(parent)

        layout = QVBoxLayout(self)

        # nice widget for editing the date
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.datetime)

        # OK and Cancel buttons
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        layout.addWidget(self.buttons)

        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

    # get current date and time from the dialog
    def dateTime(self):
        return self.datetime.dateTime()

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getDateTime(parent = None):
        dialog = DateDialog(parent)
        result = dialog.exec_()
        date = dialog.dateTime()
        return (date.date(), date.time(), result == QDialog.Accepted)

if __name__ == "__main__":
    app = QApplication([])
    date, time, ok = DateDialog.getDateTime()
    print("{} {} {}".format(date, time, ok))
    app.exec_()