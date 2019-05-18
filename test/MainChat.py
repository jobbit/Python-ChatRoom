# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainChat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import GroupOperation

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(743, 622)
        self.Dialog = Dialog
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(60, 40, 111, 361))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(170, 40, 481, 361))
        self.tableView.setObjectName("tableView")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(60, 400, 111, 131))
        self.toolButton.setObjectName("toolButton")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(540, 400, 111, 131))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(170, 400, 371, 131))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(60, 10, 591, 31))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "User1"))
        item = self.listWidget.item(1)
        item.setText(_translate("Dialog", "User2"))
        item = self.listWidget.item(2)
        item.setText(_translate("Dialog", "User3"))
        #self.listWidget.itemClicked.connect ( self.jump_to_GroupOperation )
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.toolButton.setText(_translate("Dialog", "+"))
        self.toolButton.clicked.connect(self.jump_to_GroupOperation)
        self.pushButton.setText(_translate("Dialog", "send"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GroupNum</p></body></html>"))

    def jump_to_GroupOperation(self):
        self.Dialog.hide()
        form1 = QtWidgets.QDialog()
        ui = GroupOperation.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.Dialog.show()

    def exit(self):
        self.Dialog.close ()

'''if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication( sys.argv )
    widget = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi( widget )
    widget.show()
    sys.exit( app.exec_ () )'''