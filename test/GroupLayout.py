# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GroupLayout.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import GroupOperation

import sys
import MainChat

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(140, 630)
        self.Dialog = Dialog
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(0, 500, 141, 131))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 141, 501))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "+"))
        self.pushButton.clicked.connect(self.jump_to_GroupOperation)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "New Item"))
        item = self.listWidget.item(1)
        item.setText(_translate("Dialog", "New Item"))
        item = self.listWidget.item(2)
        item.setText(_translate("Dialog", "New Item"))
        self.listWidget.itemClicked.connect ( self.jump_to_MainChat)
        self.listWidget.setSortingEnabled(__sortingEnabled)

    def jump_to_GroupOperation(self):
        self.Dialog.hide()
        form1 = QtWidgets.QDialog()
        ui = GroupOperation.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.Dialog.show()

    def jump_to_MainChat(self):
        self.Dialog.close ()
        form1 = QtWidgets.QDialog()
        ui = MainChat.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.Dialog.close ()

if __name__ == "__main__":
    app = QtWidgets.QApplication( sys.argv )
    widget = QtWidgets.QWidget()
    window = Ui_Dialog()
    window.setupUi( widget )
    widget.show()
    sys.exit( app.exec_ () )