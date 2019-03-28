# coding = utf-8
from PyQt5.QtWidgets import *
import sys
import app.webchatapp

qt_app = QApplication(sys.argv)

webchat = app.webchatapp.WebChatApp()

sys.exit(qt_app.exec())
