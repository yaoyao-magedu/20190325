# coding = utf-8
from PyQt5.QtCore import *
from uis.widwebchatmain import *
from uis.dlgqrlogin import *
from tencents.webchathelper import *
class WebChatApp:
    current_user = None
    def __init__(self):
        super().__init__()
        self.chat = WebChatHelper()
        self.ui_login = DlgQRLogin(self.chat)
        self.ui_main = WidWebChatMain(self.chat)
        
        self.ui_login.show()
        self.ui_main.hide()
