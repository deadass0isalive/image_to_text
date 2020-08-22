import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from mainwindow import Ui_MainWindow
import extract
import os


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.preview_button.setEnabled(False)
        self.ui.convert_button.setEnabled(False)
        self.ui.path_edit.textEdited.connect(self.enable_preview_button)
        self.ui.browse_button.clicked.connect(self.browse_button_clicked)
        self.ui.preview_button.clicked.connect(self.preview_button_clicked)
        self.ui.convert_button.clicked.connect(self.get_string)

    # logic when browse button is clicked
    def browse_button_clicked(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Select Image', "/home", "Images (*.png *.jpeg *.jpg)")
        if fileName != "":
            self.ui.path_edit.setText(fileName)
            self.ui.preview_button.setEnabled(True)
        else:
            msg = QMessageBox()
            msg.about(self, 'Error', "File PATH can't be empty, Please select Image File")

    # logic when preview button clicked
    def preview_button_clicked(self):
        path = self.ui.path_edit.text()

        if os.path.isfile(path):
            # below line if file exist enable convert button
            self.ui.convert_button.setEnabled(True)

            self.ui.preview_label.setPixmap(QPixmap(path))
        else:
            msg = QMessageBox()
            msg.about(self, 'Error', "Invalid File, Please select Valid Image File")

    def enable_preview_button(self):
        if self.ui.path_edit.text() != "":
            self.ui.preview_button.setEnabled(True)
        else:
            self.ui.preview_button.setEnabled(False)

    def get_string(self):
        path = self.ui.path_edit.text()

        if os.path.isfile(path):
            self.ui.textedit.setText(extract.return_string(path))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
