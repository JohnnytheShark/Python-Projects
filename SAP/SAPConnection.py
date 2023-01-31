import sys, win32com.client as win32, time
import subprocess

class SAPGUI():
    # def __init__():None
    # pass 

    def connect_sap(self):
        self.SapGuiAuto = win32.GetObject("SAPGUI")
        application = self.SapGuiAuto.GetScriptingEngine
        self.connection = application.OpenConnection(ConnectionType,True)
        time.sleep(3)
        self.session = self.connection.Children(0)

    def __open_sap(self):
        subprocess.Popen(SAPApplication)

    def connect_to_current_openwindow(self):
        self.SapGuiAuto = win32.GetObject("SAPGUI")
        application = self.SapGuiAuto.GetScriptingEngine
        self.connection = application.Children(0)
        self.session = self.connection.Children(0)
    
    def sap_login(self):
        self.__open_sap()
        time.sleep(5)
        self.connect_sap()
        time.sleep(5)
        self.session.findById("wnd[0]/usr/txtRSYST-BNAME").text = User
        self.session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = Password
        self.session.findById("wnd[0]").sendVKey(0)
