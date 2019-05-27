# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MainChat
import LoginError
import Register
import GroupLayout

import gol

import sys
import requests
import json


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Di+alog")
        Dialog.resize(394, 258)
        self.Dialog = Dialog
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 54, 12))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 210, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 210, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(60, 150, 171, 16))
        self.checkBox.setObjectName("checkBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 40, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 90, 181, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "用户名："))
        self.label_2.setText(_translate("Dialog", "密码："))
        self.pushButton.setText(_translate("Dialog", "注册"))
        self.pushButton.clicked.connect (self.jump_to_Register)
        self.pushButton_2.setText(_translate("Dialog", "确定"))
        self.pushButton_2.clicked.connect(self.check)
        self.checkBox.setText(_translate("Dialog", "记住用户名和密码"))

    def Token_User(self):
        global hed
        global token
        global auth_token
        global url
        global groups

        url = 'http://www.lunareclipse.net.cn:8000'
        gol.set_value('url',url)
        # token
        api = '/api/token'
        email = self.lineEdit.text ()
        password = self.lineEdit_2.text ()
        r = requests.post ( url + api, auth=(email, password) )

        auth_token = r.json ()['token']
        hed = {'Authorization': 'Bearer ' + auth_token}
        gol.set_value('hed',hed)

        # 获取用户信息
        api = '/api/user/6'
        print ( auth_token )
        print ( hed )
        r = requests.get ( url + api, headers=hed )
        token = r.json()
        print ( "获取用户信息" )
        print ( token )

        # 获取用户群组信息
        api = '/api/groups'
        r = requests.get ( url + api, headers=hed )
        groups = r.json()
        gol.set_value('groups',groups)
        print ( "获取用户群组信息" )
        print ( r.text )
        print ( groups )

    def check(self):
        #self.jump_to_GroupLayout ()

        self.Token_User()
        global token
        print(token)
        if  'id' in token:
            self.jump_to_GroupLayout()
        else:
            self.jump_to_LoginError()

    def jump_to_MainChat(self):
        self.Dialog.close ()
        id = self.lineEdit.text ()
        password = self.lineEdit_2.text ()
        print (id,password)
        form1 = QtWidgets.QDialog()
        ui = MainChat.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.Dialog.close ()

    def jump_to_Register(self):
        self.Dialog.close()
        form1 = QtWidgets.QDialog()
        ui = Register.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.Dialog.show()

    def jump_to_LoginError(self):
        self.Dialog.close ()
        form1 = QtWidgets.QDialog()
        ui = LoginError.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.Dialog.close ()

    def jump_to_GroupLayout(self):
        self.Dialog.close ()
        form1 = QtWidgets.QDialog()
        ui = GroupLayout.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.Dialog.close ()

    def exit(self):
        self.Dialog.close ()


if __name__ == "__main__":
    gol._init()
    app = QtWidgets.QApplication( sys.argv )
    widget = QtWidgets.QWidget()
    window = Ui_Dialog()
    window.setupUi( widget )
    widget.show()
    sys.exit( app.exec_ () )
