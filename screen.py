# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QDesktopWidget
# # from shapes import Ui_Form
# # from carry import Ui_Carry
# from confirmation import Ui_confirmation
# import variables
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("GEDI")
#         MainWindow.resize(640, 480)
#         MainWindow.setWindowTitle('GEDI')
#
#         # moving position of window to center of screen
#         frame = MainWindow.frameGeometry()
#         center = QDesktopWidget().availableGeometry().center()
#         frame.moveCenter(center)
#         MainWindow.move(frame.topLeft())
#
#         # Setting MainWindow Graphics
#         MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setStyleSheet("background-color: white")
#         self.centralwidget.setObjectName("centralwidget")
#         self.Scout = QtWidgets.QPushButton(MainWindow)
#         self.Scout.setStyleSheet("background-color:black; color: red")
#         self.Scout.setGeometry(QtCore.QRect(40, 250, 250, 100))
#         self.Scout.setObjectName("Scout")
#         self.Tile = QtWidgets.QPushButton(MainWindow)
#         self.Tile.setStyleSheet("background-color:black; color: red")
#         self.Tile.setGeometry(QtCore.QRect(340, 250, 250, 100))
#         self.Tile.setObjectName("Tile Placer")
#         self.Carry = QtWidgets.QPushButton(MainWindow)
#         self.Carry.setStyleSheet("background-color:black; color: red")
#         self.Carry.setGeometry(QtCore.QRect(340, 90, 250, 100))
#         self.Carry.setObjectName("Carry")
#         self.Shapes = QtWidgets.QPushButton(MainWindow)
#         self.Shapes.setStyleSheet("background-color:black; color: red")
#         self.Shapes.setGeometry(QtCore.QRect(40, 90, 250, 100))
#         self.Shapes.setObjectName("Shapes")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 22))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#         # Connecting Clicked Buttons
#         self.Shapes.clicked.connect(self.shapes)
#         self.Carry.clicked.connect(self.carry)
#         self.Scout.clicked.connect(self.scout)
#         self.Tile.clicked.connect(self.tile)
#
#     def MainShow(self):
#         self.MainWindow = QtWidgets.QMainWindow()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self.MainWindow)
#         self.MainWindow.show()
#
#     # def shapes(self):
#     #     self.Form = QtWidgets.QWidget()
#     #     self.ui = Ui_Form()
#     #     self.ui.setupUi(self.Form)
#     #     self.Form.show()
#
#     # def carry(self):
#     #     self.Carry = QtWidgets.QWidget()
#     #     self.ui = Ui_Carry()
#     #     self.ui.setupUi(self.Carry)
#     #     self.Carry.show()
#
#     def scout(self, confirmation):
#         variables.command = 8
#         # function to show screen/widget
#         variables.widget = 1
#         variables.ScreenWidget.setCurrentIndex(variables.widget)
#         variables.ScreenWidget.show()
#
#     def tile(self):
#         variables.command = 9
#         # Ui_confirmation.ConfirmationShow(self)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.Scout.setText(_translate("MainWindow", "Scout"))
#         self.Tile.setText(_translate("MainWindow", "Tile"))
#         self.Carry.setText(_translate("MainWindow", "Carry"))
#         self.Shapes.setText(_translate("MainWindow", "Shapes"))
#
# #
# # class Ui_confirmation(object):
# #
# #     def ConfirmationShow(self, confirmation):
# #        confirmation.show()
# #
# #     def setupUi(self, confirmation):
# #         confirmation.setObjectName("confirmation")
# #         confirmation.resize(300, 200)
# #
# #         #moving position of window to center of screen
# #         frame = confirmation.frameGeometry()
# #         center = QDesktopWidget().availableGeometry().center()
# #         frame.moveCenter(center)
# #         confirmation.move(frame.topLeft())
# #
# #         self.confirm = QtWidgets.QPushButton(confirmation)
# #         self.confirm.setStyleSheet("background-color: black; color: green")
# #         self.confirm.setGeometry(QtCore.QRect(50, 30, 200, 50))
# #         self.confirm.setAutoDefault(False)
# #         self.confirm.setObjectName("confirm")
# #         self.cancel = QtWidgets.QPushButton(confirmation)
# #         self.cancel.setStyleSheet("background-color: black; color: red")
# #         self.cancel.setGeometry(QtCore.QRect(50, 110, 200, 50))
# #         self.cancel.setObjectName("cancel")
# #
# #         self.retranslateUi(confirmation)
# #         QtCore.QMetaObject.connectSlotsByName(confirmation)
# #
# #         #connecting pushed buttons to commands
# #         self.confirm.clicked.connect(self.Confirm)
# #         self.cancel.clicked.connect(self.Cancel)
# #
# #     def Confirm(self):
# #         print(variables.command)
# #
# #     def Cancel(self):
# #         variables.command = 0
# #         print(variables.command)
# #
# #     def retranslateUi(self, confirmation):
# #         _translate = QtCore.QCoreApplication.translate
# #         confirmation.setWindowTitle(_translate("confirmation", "Form"))
# #         self.confirm.setText(_translate("confirmation", "Confirm"))
# #         self.cancel.setText(_translate("confirmation", "Cancel"))
#
#
#
#
#
# if __name__ == "__main__":
#
#     while True:
#         import sys
#
#         exit = 0
#         app = QtWidgets.QApplication(sys.argv)
#         MainWindow = QtWidgets.QMainWindow()
#         ui = Ui_MainWindow()
#         ui.setupUi(MainWindow)
#         MainWindow.show()
#         sys.exit(app.exec_())
#         sleep(1000000)
#
