import subprocess
import psutil
from time import sleep
import pygetwindow as gw
import pyautogui
import keyboard
import sys

from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('untitled.ui', self)

        self.accountList = self.retrieveAccounts()

        for key, value in self.accountList.items():
            self.comboBox.addItem(key)

        self.button1 = self.findChild(QtWidgets.QPushButton, 'loginButton')
        self.button1.clicked.connect(self.loginAccount)
        #chosenAcc = str(self.comboBox.currentText())
        #self.button1.clicked.connect(lambda: self.loginAccount(chosenAcc))

    def retrieveAccounts(self):
        accountList = {}
        with open('accounts.txt') as file:
            file_contents = file.read()
            file_output = file_contents.split('\n')
            for x in range(0, len(file_output)):
                acc_name = file_output[x].split(':')[0]
                acc_id = file_output[x].split(':')[1]
                acc_psw = file_output[x].split(':')[2]
                accountList[acc_name] = [acc_id, acc_psw]
        return accountList
            

    def loginAccount(self):
        chosenAcc = str(self.comboBox.currentText())

        pid = subprocess.Popen([r"G:\Games\Riot Games\Riot Client\RiotClientServices.exe", "--launch-product=league_of_legends", "--launch-patchline=live"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        
        if ("LeagueClientUx.exe" in (p.name() for p in psutil.process_iter())):
            print("Already logged in.")
            pass
        else:
            while(True):
                if ("RiotClientUx.exe" in (p.name() for p in psutil.process_iter())):
                    break
                else:
                    pass
    
            while (len(gw.getWindowsWithTitle('Riot Client')) < 1):
                pass

            sleep(1)
            keyboard.write(self.accountList[chosenAcc][0])
            keyboard.press_and_release('tab')
            keyboard.write(self.accountList[chosenAcc][1])
            keyboard.press_and_release('enter')

app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()