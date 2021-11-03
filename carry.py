from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from confirmation import Ui_confirmation
import variables


class Ui_Carry(object):
    def setupUi(self, Carry):
        Carry.setObjectName("Carry")
        Carry.resize(640, 480)

        #moving position of window to center of screen
        frame = Carry.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center)
        Carry.move(frame.topLeft())

        self.pushButton = QtWidgets.QPushButton(Carry)
        self.pushButton.setStyleSheet("background-color: black; color: red; font-size: 32px")
        self.pushButton.setGeometry(QtCore.QRect(25, 100, 250, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Carry)
        self.pushButton_2.setStyleSheet("background-color: black; color: green; font-size: 32px")
        self.pushButton_2.setGeometry(QtCore.QRect(350, 100, 250, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Carry)
        self.pushButton_3.setStyleSheet("background-color: black; color: blue; font-size: 32px")
        self.pushButton_3.setGeometry(QtCore.QRect(200, 250, 250, 100))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Carry)
        QtCore.QMetaObject.connectSlotsByName(Carry)

        #Button Connecting/Setting Up
        self.pushButton.clicked.connect(self.Red)
        self.pushButton_2.clicked.connect(self.Blue)
        self.pushButton_3.clicked.connect(self.Green)


    def Red(self):
        variables.command = 5
        self.confirmation = QtWidgets.QWidget()
        self.ui = Ui_confirmation()
        self.ui.setupUi(self.confirmation)
        self.confirmation.show()

    def Green(self):
        variables.command = 6
        self.confirmation = QtWidgets.QWidget()
        self.ui = Ui_confirmation()
        self.ui.setupUi(self.confirmation)
        self.confirmation.show()

    def Blue(self):
        variables.command = 7
        self.confirmation = QtWidgets.QWidget()
        self.ui = Ui_confirmation()
        self.ui.setupUi(self.confirmation)
        self.confirmation.show()

    def retranslateUi(self, Carry):
        _translate = QtCore.QCoreApplication.translate
        Carry.setWindowTitle(_translate("Carry", "Form"))
        self.pushButton.setText(_translate("Carry", "Red"))
        self.pushButton_2.setText(_translate("Carry", "Green"))
        self.pushButton_3.setText(_translate("Carry", "Blue"))


