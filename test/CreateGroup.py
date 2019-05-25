# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateGroup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MainChat
import gol
import requests


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.dialog = Dialog
        self.label_2 = QtWidgets.QLabel ( Dialog )
        self.label_2.setGeometry ( QtCore.QRect ( 50, 80, 54, 20 ) )
        self.label_2.setObjectName ( "label_2" )
        self.pushButton_2 = QtWidgets.QPushButton ( Dialog )
        self.pushButton_2.setGeometry ( QtCore.QRect ( 260, 240, 75, 23 ) )
        self.pushButton_2.setObjectName ( "pushButton_2" )
        self.lineEdit = QtWidgets.QLineEdit ( Dialog )
        self.lineEdit.setGeometry ( QtCore.QRect ( 120, 80, 161, 20 ) )
        self.lineEdit.setObjectName ( "lineEdit" )
        self.label = QtWidgets.QLabel ( Dialog )
        self.label.setGeometry ( QtCore.QRect ( 170, 40, 61, 21 ) )
        self.label.setObjectName ( "label" )
        self.pushButton = QtWidgets.QPushButton ( Dialog )
        self.pushButton.setGeometry ( QtCore.QRect ( 160, 170, 75, 23 ) )
        self.pushButton.setObjectName ( "pushButton" )
        self.label_3 = QtWidgets.QLabel ( Dialog )
        self.label_3.setGeometry ( QtCore.QRect ( 50, 180, 54, 12 ) )
        self.label_3.setObjectName ( "label_3" )
        self.label_4 = QtWidgets.QLabel ( Dialog )
        self.label_4.setGeometry ( QtCore.QRect ( 50, 130, 54, 12 ) )
        self.label_4.setObjectName ( "label_4" )
        self.lineEdit_2 = QtWidgets.QLineEdit ( Dialog )
        self.lineEdit_2.setGeometry ( QtCore.QRect ( 120, 130, 161, 20 ) )
        self.lineEdit_2.setObjectName ( "lineEdit_2" )

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "名称："))
        self.pushButton_2.setText(_translate("Dialog", "ok"))
        self.pushButton_2.clicked.connect ( self.CreateGroup )
        self.label.setText(_translate("Dialog", "创建群聊"))
        self.pushButton.setText(_translate("Dialog", "点击上传"))
        self.label_3.setText(_translate("Dialog", "头像："))
        self.label_4.setText(_translate("Dialog", "群id"))


    def jump_to_MainChat(self):
        self.dialog.close()
        form1 = QtWidgets.QDialog()
        ui = MainChat.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.dialog.show()

    def CreateGroup(self):
        url = gol.get_value('url')
        hed = gol.get_value('hed')
        print(hed,url)
        api = '/api/group/create'
        group_id = self.lineEdit.text ()
        group_name = self.lineEdit_2.text()
        gol.set_value ( 'GroupName', group_name )
        avatar = 'avatar'
        data = {'group_id': group_id, 'avatar': avatar, 'group_name': group_name}
        r = requests.post ( url + api, json=data, headers=hed )
        print ( "创建群组" )
        print ( r.json () )
        self.jump_to_MainChat()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication ( sys.argv )
    widget = QtWidgets.QWidget ()
    ui = Ui_Dialog ()
    ui.setupUi ( widget )
    widget.show ()
    sys.exit ( app.exec_ () )
