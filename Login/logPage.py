# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_log(object):
    def setupUi(self, log):
        log.setObjectName("log")
        log.resize(400, 300)
        self.label = QtWidgets.QLabel(log)
        self.label.setGeometry(QtCore.QRect(90, 50, 191, 141))
        self.label.setObjectName("label")

        self.retranslateUi(log)
        QtCore.QMetaObject.connectSlotsByName(log)

    def retranslateUi(self, log):
        _translate = QtCore.QCoreApplication.translate
        log.setWindowTitle(_translate("log", "Form"))
        self.label.setText(_translate("log", "LOGIN PAGE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    log = QtWidgets.QWidget()
    ui = Ui_log()
    ui.setupUi(log)
    log.show()
    sys.exit(app.exec_())

