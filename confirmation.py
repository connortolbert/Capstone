from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
import variables
import time


class Ui_confirmation(object):

    def ConfirmationShow(self):
        self.confirmation = QtWidgets.QWidget()
        self.ui = Ui_confirmation()
        self.ui.setupUi(self.confirmation)
        self.confirmation.show()

    def ConfirmationHide(self):
        # self.confirmation = QtWidgets.QWidget()
        # self.ui = Ui_confirmation()
        # self.ui.setupUi(self.confirmation)
        Ui_confirmation.hide()

    def setupUi(self, confirmation):
        confirmation.setObjectName("confirmation")
        confirmation.resize(300, 200)

        #moving position of window to center of screen
        frame = confirmation.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center)
        confirmation.move(frame.topLeft())

        self.confirm = QtWidgets.QPushButton(confirmation)
        self.confirm.setStyleSheet("background-color: black; color: green")
        self.confirm.setGeometry(QtCore.QRect(50, 30, 200, 50))
        self.confirm.setAutoDefault(False)
        self.confirm.setObjectName("confirm")
        self.cancel = QtWidgets.QPushButton(confirmation)
        self.cancel.setStyleSheet("background-color: black; color: red")
        self.cancel.setGeometry(QtCore.QRect(50, 110, 200, 50))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(confirmation)
        QtCore.QMetaObject.connectSlotsByName(confirmation)

        #connecting pushed buttons to commands
        self.confirm.clicked.connect(self.Confirm)
        self.cancel.clicked.connect(self.Cancel)




    def Confirm(self):
        print(variables.command)
        # ConfirmationHide()
        print("Encoded")
        variables.s.send(str(variables.command).encode())
        print("Sent")
        time.sleep(3)

    def Cancel(self):
        variables.command = 0
        print(variables.command)
        msg = variables.s.recv(50)
        time.sleep(3)



    def retranslateUi(self, confirmation):
        _translate = QtCore.QCoreApplication.translate
        confirmation.setWindowTitle(_translate("confirmation", "Form"))
        self.confirm.setText(_translate("confirmation", "Confirm"))
        self.cancel.setText(_translate("confirmation", "Cancel"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#
#     sys.exit(app.exec_())
# confirmation = Ui_confirmation
# variables.ScreenWidget.addWidget(confirmation)
# confirmation2 = QtWidgets.QWidget()
# conUi = Ui_confirmation()
# conUi.setupUi(confirmation2)