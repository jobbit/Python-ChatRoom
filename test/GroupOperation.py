# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GroupOperation.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import JoinGroup
import CreateGroup
import MainChat

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.Dialog = Dialog
        self.pushButton_Create_Group = QtWidgets.QPushButton(Dialog)
        self.pushButton_Create_Group.setGeometry(QtCore.QRect(20, 40, 161, 101))
        self.pushButton_Create_Group.setObjectName("pushButton_Create_Group")
        self.pushButton_Join_Group = QtWidgets.QPushButton(Dialog)
        self.pushButton_Join_Group.setGeometry(QtCore.QRect(220, 40, 161, 101))
        self.pushButton_Join_Group.setObjectName("pushButton_Join_Group")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_Create_Group.setText(_translate("Dialog", "创建群聊"))
        self.pushButton_Create_Group.clicked.connect(self.jump_to_CreateGroup)
        self.pushButton_Join_Group.setText(_translate("Dialog", "加入群聊"))
        self.pushButton_Join_Group.clicked.connect(self.jump_to_JoinGroup )
        self.pushButton.setText(_translate("Dialog", "取消"))
        self.pushButton.clicked.connect(self.Dialog.close)

    def jump_to_CreateGroup(self):
        self.Dialog.close()
        form1 = QtWidgets.QDialog()
        ui = CreateGroup.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.Dialog.show()

    def jump_to_JoinGroup(self):
        self.Dialog.close()
        form2 = QtWidgets.QDialog()
        ui = JoinGroup.Ui_Dialog()
        ui.setupUi(form2)
        form2.show()
        form2.exec_()
        self.Dialog.show()

    def jump_to_MainChat(self):
        self.Dialog.close()
        form1 = QtWidgets.QDialog()
        ui = MainChat.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.Dialog.show()


