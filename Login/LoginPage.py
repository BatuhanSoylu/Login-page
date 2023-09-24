from PyQt5 import QtWidgets,uic
import sys
from functions import registerf,getdata,check_code_And_Update_Password,loginPage_check

class login(QtWidgets.QDialog):
    def __init__(self):
        super(login, self).__init__()
        uic.loadUi('DialogLogin.ui',self)
        self.btnRegister.clicked.connect(self.reg)
        self.btnForget.clicked.connect(self.forg)
        self.btnLogin.clicked.connect(self.log)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
    def log(self):
        number=loginPage_check(self.txtUsername.text(),self.txtPassword.text())
        print(number)
        if number==1:
            lo=logAfter()
            widget.addWidget(lo)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            print("sorry try again....")
    def reg(self):
        regis=register()
        widget.addWidget(regis)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def forg(self):
        fo=forget()
        widget.addWidget(fo)
        widget.setCurrentIndex(widget.currentIndex()+1)

class logAfter(QtWidgets.QDialog):
    def __init__(self):
        super(logAfter, self).__init__()
        uic.loadUi('DialogLogAfter.ui',self)

class register(QtWidgets.QDialog):
    def __init__(self):
        super(register, self).__init__()
        uic.loadUi('DialogRegister.ui',self)
        #self.btnRegisterInPage.clicked.connect(self.registerf(self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text()))
        self.btnRegisterInPage.clicked.connect(self.regg)
        log = login()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def regg(self):
        registerf(self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text())
        log=login()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)

class forget(QtWidgets.QDialog):
    def __init__(self):
        super(forget, self).__init__()
        uic.loadUi('DialogForget.ui',self)
        self.btnMail.clicked.connect(self.mail)
        self.btnSavePassword.clicked.connect(self.save)
        log=login()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def mail(self):
        getdata(self.txtUsername.text())
    def save(self):
        check_code_And_Update_Password(self.txtCode.text(),self.txtPassword.text(),self.txtPasswordCheck.text(),self.txtUsername.text())


        log=login()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)


app = QtWidgets.QApplication(sys.argv)
window = login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedWidth(600)
widget.setFixedHeight(600)
widget.show()
app.exec_()
