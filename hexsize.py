from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from confirmation import Ui_confirmation
import variables


class Ui_HexSize(object):
    def setupUi(self, HexSize):
        HexSize.setObjectName("Carry")
        HexSize.resize(640, 480)

        #moving position of window to center of screen
        frame = HexSize.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center)
        HexSize.move(frame.topLeft())

        #Button Creation, Placement, Naming, Styling
        self.pushButton = QtWidgets.QPushButton(HexSize)
        self.pushButton.setStyleSheet("background-color:black; color: red; font-size: 32px")
        self.pushButton.setGeometry(QtCore.QRect(120, 50, 400, 175))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(HexSize)
        self.pushButton_2.setStyleSheet("background-color:black; color: red; font-size: 32px")
        self.pushButton_2.setGeometry(QtCore.QRect(120, 250, 400, 175))
        self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_3 = QtWidgets.QPushButton(HexSize)
        # self.pushButton_3.setStyleSheet("background-color:black; color: red; font-size: 32px")
        # self.pushButton_3.setGeometry(QtCore.QRect(200, 250, 250, 100))
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.pushButton_4 = QtWidgets.QPushButton(HexSize)
        # self.pushButton_4.setStyleSheet("background-color: red;" "color: white")
        # self.pushButton_4.setGeometry(QtCore.QRect(300, 185, 80, 40))
        # self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(HexSize)
        QtCore.QMetaObject.connectSlotsByName(HexSize)

        #Connecting Clicked Buttons
        self.pushButton.clicked.connect(self.Small)
        self.pushButton_2.clicked.connect(self.Medium)
        # self.pushButton_3.clicked.connect(self.Large)
        # self.pushButton_4.clicked.connect(self.Back)

    #Command Functions: what happens when a button is pressed
    #Adding decimals to command in order to use as time later in scripts
    def Small(self):
        variables.command = variables.command + 0.05
        Ui_confirmation.ConfirmationShow(self)


    def Medium(self):
        variables.command = variables.command + 0.1
        Ui_confirmation.ConfirmationShow(self)


    # def Large(self):
    #     variables.command = variables.command + 0.6
    #     Ui_confirmation.ConfirmationShow(self)



    #Setting Button text
    def retranslateUi(self, HexSize):
        _translate = QtCore.QCoreApplication.translate
        HexSize.setWindowTitle(_translate("HexSize", "HexSize"))
        self.pushButton.setText(_translate("HexSize", "R = 1/3 m"))
        self.pushButton_2.setText(_translate("HexSize", "R = 1/2 m"))
        # self.pushButton_3.setText(_translate("HexSize", "R = 1 m"))
        # self.pushButton_4.setText(_translate("HexSize", "Back"))

