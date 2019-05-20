# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Login
import requests
import RegisterError
import operator
import sys
import json

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.Dialog = Dialog
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(180, 10, 71, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 110, 191, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 60, 54, 12))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 60, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 160, 191, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 210, 191, 20))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 210, 91, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "再次输入密码："))
        self.label_4.setText(_translate("Dialog", "注册"))
        self.label.setText(_translate("Dialog", "用户名："))
        self.pushButton.setText(_translate("Dialog", "ok"))
        self.pushButton.clicked.connect ( self.jump_to_Login )
        self.label_2.setText(_translate("Dialog", "密码："))
        self.label_5.setText ( _translate ( "Dialog", "昵称：" ) )

    def jump_to_Login(self):
        id = self.lineEdit.text ()
        password = self.lineEdit_2.text ()
        repassword = self.lineEdit_3.text ()
        nickname = self.lineEdit_4.text ()
        if operator.eq(password,repassword):
            print('ok')
            self.Register_User ()
            print ( id, password, repassword, nickname )
            self.Dialog.close ()
            form1 = QtWidgets.QDialog ()
            ui = Login.Ui_Dialog ()
            ui.setupUi ( form1 )
            form1.show ()
            form1.exec_ ()
            self.Dialog.show ()
        else:
            print('error')
            self.jump_to_RegisterError()

    def jump_to_RegisterError(self):
        self.Dialog.hide()
        form1 = QtWidgets.QDialog()
        ui = RegisterError.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.Dialog.show()

    def Register_User(self):
        url = 'http://www.lunareclipse.net.cn:8000'
        api = '/api/user'
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        nickname = self.lineEdit_4.text()
        data = {'email': email, "password": password, "nickname": nickname,
                'avatar': 'https://i.loli.net/2019/05/20/5ce24d067e55d75476.png'}
        r = requests.post ( url + api, json=data )
        print ( r.json () )

if __name__ == "__main__":
    app = QtWidgets.QApplication( sys.argv )
    widget = QtWidgets.QWidget()
    window = Ui_Dialog()
    window.setupUi( widget )
    widget.show()
    sys.exit( app.exec_ () )