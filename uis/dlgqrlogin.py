# coding = utf-8

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from uis import ui_login
# import ui_login
import sys
class DlgQRLogin(QDialog):
    def __init__(self, chat_, parent = None):
        super().__init__(parent = parent)
        self.chat = chat_
        self.ui_login = ui_login.Ui_ui_login()
        self.ui_login.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        # self.show()


# app = QApplication(sys.argv)
# dlg = DlgQRLogin()
# app.exec()