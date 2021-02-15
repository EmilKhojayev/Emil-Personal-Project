from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys

app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(0, 0, 1920, 1080)
win.setWindowTitle('TISA Scoreboard')


def loginin():
    if Username.text() == 'SRAA' and Password.text() == 'TISA2021':
        print('ok')
        Userlabel.hide()
        Passlabel.hide()
        Username.hide()
        Password.hide()
        Login.hide()
        MySuperCoolControl.show()




font = QtGui.QFont()
font.setFamily("Sitka Text")
font.setPointSize(22)
font.setBold(True)
font.setWeight(75)


Userlabel = QtWidgets.QLabel(win)
Userlabel.setText("Username:")
Userlabel.setFont(font)
Userlabel.resize(230, 50)
Userlabel.move(710, 375)

Passlabel = QtWidgets.QLabel(win)
Passlabel.setText('Password:')
Passlabel.setFont(font)
Passlabel.resize(225, 50)
Passlabel.move(720, 440)

Username = QtWidgets.QLineEdit(win)
Username.setFont(font)
Username.resize(220, 50)
Username.move(950, 380)

Password = QtWidgets.QLineEdit(win)
Password.setFont(font)
Password.resize(220, 50)
Password.move(950, 450)

Login = QtWidgets.QPushButton(win)
Login.setFont(font)
Login.resize(460, 70)
Login.setText('Login')
Login.move(710, 530)
Login.clicked.connect(loginin)

MySuperCoolControl = QtWidgets.QLabel(win)
MySuperCoolControl.setFont(font)
MySuperCoolControl.resize(400,70)
MySuperCoolControl.move(100, 100)
MySuperCoolControl.setText('My App will start here!')
MySuperCoolControl.hide()


win.show()

sys.exit(app.exec_())
