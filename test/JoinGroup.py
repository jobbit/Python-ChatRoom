# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JoinGroup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MainChat

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.dialog = Dialog
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 30, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 54, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 230, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 110, 161, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "加入群聊"))
        self.label_2.setText(_translate("Dialog", "群号码："))
        self.pushButton_2.setText(_translate("Dialog", "ok"))
        self.pushButton_2.clicked.connect ( self.jump_to_MainChat )

    def jump_to_MainChat(self):
        GroupNum = self.lineEdit.text ()
        print(GroupNum)
        self.dialog.close()
        form1 = QtWidgets.QDialog()
        ui = MainChat.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.dialog.show()

