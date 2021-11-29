import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from shapes import Ui_Form
from carry import Ui_Carry
from confirmation import Ui_confirmation
import variables
import time
import socket


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("GEDI")
        MainWindow.resize(640, 480)
        MainWindow.setWindowTitle('GEDI')

        #moving position of window to center of screen
        frame = MainWindow.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center)
        MainWindow.move(frame.topLeft())

        #Setting MainWindow Graphics
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: white")
        self.centralwidget.setObjectName("centralwidget")

        #Creating and Configuring Buttons
        self.Scout = QtWidgets.QPushButton(MainWindow)
        self.Scout.setStyleSheet("background-color:black; color: red; font-size: 32px")
        self.Scout.setGeometry(QtCore.QRect(40, 250, 250, 100))
        self.Scout.setObjectName("Scout")
        self.Tile = QtWidgets.QPushButton(MainWindow)
        self.Tile.setStyleSheet("background-color:black; color: red; font-size: 32px")
        self.Tile.setGeometry(QtCore.QRect(340, 250, 250, 100))
        self.Tile.setObjectName("Tile Placer")
        self.Carry = QtWidgets.QPushButton(MainWindow)
        self.Carry.setStyleSheet("background-color:black; color: red; font-size: 32px")
        self.Carry.setGeometry(QtCore.QRect(340, 90, 250, 100))
        self.Carry.setObjectName("Carry")
        self.Shapes = QtWidgets.QPushButton(MainWindow)
        self.Shapes.setStyleSheet("background-color:black; color: red; font-size: 32px")
        self.Shapes.setGeometry(QtCore.QRect(40, 90, 250, 100))
        self.Shapes.setObjectName("Shapes")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Connecting Clicked Buttons
        self.Shapes.clicked.connect(self.shapes)
        self.Carry.clicked.connect(self.carry)
        self.Scout.clicked.connect(self.scout)
        self.Tile.clicked.connect(self.tile)

    #Command Functions: what happens when a button is pressed, Connecting separate windows
    def MainShow(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def shapes(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def carry(self):
        self.Carry = QtWidgets.QWidget()
        self.ui = Ui_Carry()
        self.ui.setupUi(self.Carry)
        self.Carry.show()

    def scout(self):
        variables.command = 8
        # variables.widget = 1
        Ui_confirmation.ConfirmationShow(self)

    def tile(self):
        variables.command = 9
        Ui_confirmation.ConfirmationShow(self)


    #Setting Button text
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Scout.setText(_translate("MainWindow", "Scout"))
        self.Tile.setText(_translate("MainWindow", "Tile"))
        self.Carry.setText(_translate("MainWindow", "Carry"))
        self.Shapes.setText(_translate("MainWindow", "Shapes"))






if __name__ == "__main__":

    while True:

        # #connor, connect to server
        # variables.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
        # variables.s.connect("192.168.1.23", 65530)  #host name/IP address, port
        #
        # #receive message from server
        # msg = variables.s.recv(50)
        # print(msg.decode())
        # time.sleep(3)
        #
        # exit = 0
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
        sleep(1000000)

