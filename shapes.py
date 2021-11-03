from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from hexsize import Ui_HexSize
from trisize import Ui_TriSize
from sqsize import Ui_SqSize
import variables

class Ui_Form(object):
    def setupUi(self, shapes):
        shapes.setObjectName("Shapes")
        shapes.resize(640, 480)
        shapes.setWindowTitle('Shapes')

        #moving position of window to center of screen
        frame = shapes.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center)
        shapes.move(frame.topLeft())

        #Push Button creation, postion, color, and setup
        self.pushButton = QtWidgets.QPushButton(shapes)
        self.pushButton.setStyleSheet("background-color: black;" "color: red; font-size: 32px")
        self.pushButton.setGeometry(QtCore.QRect(40, 250, 250, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(shapes)
        self.pushButton_2.setStyleSheet("background-color: black;" "color: red; font-size: 32px")
        self.pushButton_2.setGeometry(QtCore.QRect(340, 250, 250, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(shapes)
        self.pushButton_3.setStyleSheet("background-color: black;" "color: red; font-size: 32px")
        self.pushButton_3.setGeometry(QtCore.QRect(340, 90, 250, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(shapes)
        self.pushButton_4.setStyleSheet("background-color: black;" "color: red; font-size: 32px")
        self.pushButton_4.setGeometry(QtCore.QRect(40, 90, 250, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        # self.pushButton_5 = QtWidgets.QPushButton(shapes)
        # self.pushButton_5.setStyleSheet("background-color: red;" "color: white")
        # self.pushButton_5.setGeometry(QtCore.QRect(300, 185, 80, 40))
        # self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(shapes)
        QtCore.QMetaObject.connectSlotsByName(shapes)

        #buttons clicked commands
        self.pushButton.clicked.connect(self.Hexagon)
        self.pushButton_2.clicked.connect(self.Triangle)
        self.pushButton_3.clicked.connect(self.Circle)
        self.pushButton_4.clicked.connect(self.Square)
        # self.pushButton_5.clicked.connect(self.Back)

    def Hexagon(self):
        variables.command = 1
        print(variables.command)
        self.HexSize = QtWidgets.QWidget()
        self.ui = Ui_HexSize()
        self.ui.setupUi(self.HexSize)
        self.HexSize.show()

    def Triangle(self):
        variables.command = 2
        self.TriSize = QtWidgets.QWidget()
        self.ui = Ui_TriSize()
        self.ui.setupUi(self.TriSize)
        self.TriSize.show()

    def Circle(self):
        variables.command = 3
        self.HexSize = QtWidgets.QWidget()
        self.ui = Ui_HexSize()
        self.ui.setupUi(self.HexSize)
        self.HexSize.show()

    def Square(self):
        variables.command = 4
        self.SqSize = QtWidgets.QWidget()
        self.ui = Ui_SqSize()
        self.ui.setupUi(self.SqSize)
        self.SqSize.show()

    # def shapesHide(self):
    #     self.Form = QtWidgets.QWidget()
    #     self.ui = Ui_Form()
    #     self.ui.setupUi(self.Form)
    #     self.Form.hide()

    # def Back(self):
    #     print("return to main")
    #     variables.command = 0
    #     print(variables.command)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Shapes", "Shapes"))
        self.pushButton.setText(_translate("Shapes", "Hexagon"))
        self.pushButton_2.setText(_translate("Shapes", "Triangle"))
        self.pushButton_3.setText(_translate("Shapes", "Circle"))
        self.pushButton_4.setText(_translate("Shapes", "Square"))
        # self.pushButton_5.setText(_translate("Shapes", "Back"))

