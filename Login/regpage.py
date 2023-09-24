# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functions import registerf
class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(566, 504)
        self.label = QtWidgets.QLabel(Register)
        self.label.setGeometry(QtCore.QRect(4, 50, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Register)
        self.label_2.setGeometry(QtCore.QRect(4, 100, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Register)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Register)
        self.label_4.setGeometry(QtCore.QRect(14, 240, 61, 20))
        self.label_4.setObjectName("label_4")
        self.btnRegisterInPage = QtWidgets.QPushButton(Register,clicked=lambda : registerf(self.lineEdit.text(),
                                                                                           self.lineEdit_2.text(),
                                                                                           self.lineEdit_3.text(),
                                                                                           self.lineEdit_4.text()))
        self.btnRegisterInPage.setGeometry(QtCore.QRect(220, 400, 93, 28))
        self.btnRegisterInPage.setObjectName("btnRegisterInPage")
        self.lineEdit = QtWidgets.QLineEdit(Register)
        self.lineEdit.setGeometry(QtCore.QRect(130, 50, 311, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Register)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 100, 311, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Register)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 170, 311, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Register)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 250, 311, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Form"))
        self.label.setText(_translate("Register", "Username"))
        self.label_2.setText(_translate("Register", "E-mail"))
        self.label_3.setText(_translate("Register", "Password"))
        self.label_4.setText(_translate("Register", "Password"))
        self.btnRegisterInPage.setText(_translate("Register", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QWidget()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())

