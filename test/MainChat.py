# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainChat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import GroupOperation
import GroupLayout
import time
import requests
import gol


class Ui_Dialog(object):
    global token
    def setupUi(self, Dialog):
        Dialog.setObjectName ( "Dialog" )
        Dialog.resize ( 629, 574 )
        self.Dialog = Dialog
        self.listWidget = QtWidgets.QListWidget ( Dialog )
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 111, 361))
        self.listWidget.setObjectName ( "listWidget" )
        self.toolButton = QtWidgets.QToolButton ( Dialog )
        self.toolButton.setGeometry(QtCore.QRect(20, 480, 111, 71))
        self.toolButton.setObjectName ( "toolButton" )
        self.pushButton = QtWidgets.QPushButton ( Dialog )
        self.pushButton.setGeometry ( QtCore.QRect ( 500, 420, 111, 131 ) )
        self.pushButton.setObjectName ( "pushButton" )
        self.plainTextEdit = QtWidgets.QPlainTextEdit ( Dialog )
        self.plainTextEdit.setGeometry ( QtCore.QRect (130, 420, 371, 131) )
        self.plainTextEdit.setObjectName ( "plainTextEdit" )
        self.textBrowser = QtWidgets.QTextBrowser ( Dialog )
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 591, 40))
        self.textBrowser.setObjectName ( "textBrowser" )
        self.listWidget_2 = QtWidgets.QListWidget ( Dialog )
        self.listWidget_2.setGeometry ( QtCore.QRect (130, 60, 481, 361) )
        self.listWidget_2.setObjectName ( "listWidget_2" )
        self.pushButton_2 = QtWidgets.QPushButton ( Dialog )
        self.pushButton_2.setGeometry ( QtCore.QRect ( 20, 420, 111, 67 ) )
        self.pushButton_2.setObjectName ( "pushButton_2" )

        self.retranslateUi ( Dialog )
        QtCore.QMetaObject.connectSlotsByName ( Dialog )

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.itemClicked.connect ( self.jump_to_GroupOperation )
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.toolButton.setText(_translate("Dialog", "+"))
        self.toolButton.clicked.connect(self.jump_to_GroupOperation)
        self.pushButton.setText(_translate("Dialog", "send"))
        self.pushButton_2.setText ( _translate ( "Dialog", "-" ) )
        self.SelfGroupLayout()
        group_name = gol.get_value ( 'GroupName' )
        group_id = gol.get_value('GroupId')
        print ( group_name )
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+group_name+"<br/>"+group_id+"</p></body></html>"))
        self.pushButton.clicked.connect(self.SelfChatSend)
        self.pushButton_2.clicked.connect(self.QuitChat)
        __sortingEnabled = self.listWidget_2.isSortingEnabled ()
        self.listWidget_2.setSortingEnabled ( False )
        self.listWidget_2.setSortingEnabled ( __sortingEnabled )
        t = threading.Thread(target=self.ReceiveMessage)
        t.start()

    def jump_to_GroupOperation(self):
        self.Dialog.close()
        form1 = QtWidgets.QDialog()
        ui = GroupOperation.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.Dialog.show()

    def jump_to_GroupLayout(self):
        self.Dialog.close()
        form1 = QtWidgets.QDialog()
        ui = GroupLayout.Ui_Dialog()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.Dialog.show()


    def PrintTime(self):
        NowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        return NowTime


    def SelfChatSend(self):
        print('进SelfSend')
        if not len(self.plainTextEdit.toPlainText()) == 0:
            print ( self.plainTextEdit.toPlainText () )
            self.listWidget_2.addItem ( self.PrintTime () )
            self.listWidget_2.addItem ( self.plainTextEdit.toPlainText () )
            self.SendMessage()

    def SelfGroupLayout(self):
        global url
        global hed
        global group_id
        url = gol.get_value('url')
        hed = gol.get_value('hed')
        api = '/api/group'
        group_id = gol.get_value('GroupId')
        print(group_id)
        page = 1
        per_page = 10
        data = {'group_id': group_id, 'page': page, 'per_page': per_page}

        r = requests.post ( url + api, json=data, headers=hed )
        print ( "获取指定分组包括组员的群组信息" )
        print ( r.json () )

        global GroupPage
        GroupPage = r.json()
        if not 'items' in GroupPage == None:
            member = GroupPage['items']
            print('群成员为',member)
            for line in member:
                if not line['nickname'] == None:
                    GroupMemberName = line['nickname']
                    print('群成员具体nickname为',GroupMemberName)
                    self.listWidget.addItem ( GroupMemberName )

    def SendMessage(self):
        global hed
        global token
        global auth_token
        global url
        global group_id
        group_id = gol.get_value('GroupId')
        url = gol.get_value('url')
        hed = gol.get_value('hed')
        api = '/api/message/send'
        content = self.plainTextEdit.toPlainText ()
        data = {'group_id': group_id, 'content': content}
        r = requests.post ( url + api, json=data, headers=hed )
        print ( "发送消息" )
        print ( r.json () )

    def ReceiveMessage(self):
        global group_id
        global url
        global hed
        print('进ReceiveMessage')
        api = '/api/message/group'
        data = {'group_id': group_id}
        r = requests.post ( url + api, json=data, headers=hed )
        print ( "获取指定群聊详细信息" )
        print ( r.json () )
        content = r.json ()
        middle = content
        if not 'items' in content == None:
            contentitem = content['items'][::-1]
            print ( '聊天item为', contentitem )
            for line in contentitem:
                if not line['content'] == None:
                    ReceiveMC = str ( line['sender']['nickname'] ) + ':' + str ( line['content'] )
                    print ( ReceiveMC )
                    ReceiveT = str ( line['created_at'] )
                    print ( ReceiveT )
                    self.listWidget_2.addItem ( ReceiveT )
                    self.listWidget_2.addItem ( ReceiveMC )
        while True:
            r1 = requests.post ( url + api, json=data, headers=hed )
            print ( "获取指定群聊详细信息" )
            print ( r1.json () )
            if not r1.json() == middle:
                content1 = r1.json()
                middle = r1.json()
                self.listWidget_2.clear ()
                if not 'items' in content1 == None:
                    contentitem = content1['items'][::-1]
                    print('聊天item为',contentitem)
                    for line1 in contentitem:
                        if not line1['content'] == None:
                            ReceiveMC = str(line1['sender']['nickname'])+':'+str(line1['content'])
                            print(ReceiveMC)
                            ReceiveT = str(line1['created_at'])
                            print(ReceiveT)
                            self.listWidget_2.addItem ( ReceiveT )
                            self.listWidget_2.addItem ( ReceiveMC )
            time.sleep(5)

    def QuitChat(self):
        # 退出群组
        global url
        global hed
        global group_id
        global t
        api = '/api/group/exit'
        page = 1
        per_page = 10
        data = {'group_id': group_id}

        r = requests.post ( url + api, json=data, headers=hed )
        print ( "退出群组" )
        print ( r.text )
        self.jump_to_GroupLayout()

    def exit(self):
        self.Dialog.close ()

if __name__ == "__main__":
    gol._init()
    import sys
    app = QtWidgets.QApplication( sys.argv )
    widget = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi( widget )
    widget.show()
    sys.exit( app.exec_ () )