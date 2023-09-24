# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from functions import getdata,check_code_And_Update_Password


class Ui_Forget(object):
    def setupUi(self, Forget):
        Forget.setObjectName("Forget")
        Forget.resize(663, 646)
        self.label_4 = QtWidgets.QLabel(Forget)
        self.label_4.setGeometry(QtCore.QRect(70, 330, 71, 21))
        self.label_4.setObjectName("label_4")
        self.btnSavePassword = QtWidgets.QPushButton(Forget,clicked=lambda:check_code_And_Update_Password(self.txtCode.text(),
                                                                                                          self.txtPassword.text(),
                                                                                                          self.txtPasswordCheck.text(),
                                                                                                          self.txtUsername.text()
                                                                                                          ))
        self.btnSavePassword.setGeometry(QtCore.QRect(300, 460, 93, 28))
        self.btnSavePassword.setObjectName("btnSavePassword")
        self.btnMail = QtWidgets.QPushButton(Forget,clicked=lambda:getdata(self.txtUsername.text()))
        self.btnMail.setGeometry(QtCore.QRect(300, 100, 93, 28))
        self.btnMail.setObjectName("btnMail")
        self.lblCode = QtWidgets.QLabel(Forget)
        self.lblCode.setGeometry(QtCore.QRect(160, 140, 381, 31))
        self.lblCode.setText("")
        self.lblCode.setObjectName("lblCode")
        self.txtPassword = QtWidgets.QLineEdit(Forget)
        self.txtPassword.setGeometry(QtCore.QRect(200, 260, 250, 22))
        self.txtPassword.setObjectName("txtPassword")
        self.txtCode = QtWidgets.QLineEdit(Forget)
        self.txtCode.setGeometry(QtCore.QRect(260, 200, 241, 22))
        self.txtCode.setObjectName("txtCode")
        self.txtPasswordCheck = QtWidgets.QLineEdit(Forget)
        self.txtPasswordCheck.setGeometry(QtCore.QRect(200, 320, 250, 22))
        self.txtPasswordCheck.setObjectName("txtPasswordCheck")
        self.label_3 = QtWidgets.QLabel(Forget)
        self.label_3.setGeometry(QtCore.QRect(70, 270, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Forget)
        self.label_5.setGeometry(QtCore.QRect(70, 200, 55, 21))
        self.label_5.setObjectName("label_5")
        self.txtUsername = QtWidgets.QLineEdit(Forget)
        self.txtUsername.setGeometry(QtCore.QRect(250, 60, 250, 22))
        self.txtUsername.setObjectName("txtUsername")
        self.label = QtWidgets.QLabel(Forget)
        self.label.setGeometry(QtCore.QRect(80, 60, 131, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Forget)
        QtCore.QMetaObject.connectSlotsByName(Forget)

    def retranslateUi(self, Forget):
        _translate = QtCore.QCoreApplication.translate
        Forget.setWindowTitle(_translate("Forget", "Form"))
        self.label_4.setText(_translate("Forget", "Password"))
        self.btnSavePassword.setText(_translate("Forget", "Save Password"))
        self.btnMail.setText(_translate("Forget", "Send Mail"))
        self.label_3.setText(_translate("Forget", "Password"))
        self.label_5.setText(_translate("Forget", "Code"))
        self.label.setText(_translate("Forget", "Username"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Forget = QtWidgets.QWidget()
    ui = Ui_Forget()
    ui.setupUi(Forget)
    Forget.show()
    sys.exit(app.exec_())

