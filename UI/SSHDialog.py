#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import QApplication, QDialog,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QFormLayout
from PyQt5 import QtCore
from Tools.SSH import SSH
import os
class SSHDialog(QDialog):
    def __init__(self):
        """
        构造函数
        """
        super(SSHDialog, self).__init__()
        self.addLine = QLineEdit('219.216.65.190')
        self.portLine = QLineEdit('22')
        self.username = QLineEdit('user2')
        self.password = QLineEdit('000000')
        connectButton = None
        self.initUI()
    def initUI(self):
        """
        定义界面
        :return:
        """
        self.setWindowTitle("SSH 连接")
        self.setGeometry(400, 400, 300, 260)
        layout = QVBoxLayout()
        formsLayout = QFormLayout()
        #self.addLine = QLineEdit()
        formsLayout.addRow("地址:", self.addLine)
        #self.portLine = QLineEdit('22')
        formsLayout.addRow("端口", self.portLine)
        #self.username = QLineEdit()
        formsLayout.addRow("用户名:", self.username)
        #self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        formsLayout.addRow('密码',self.password)
        layout.addLayout(formsLayout)
        connectButton = QPushButton('连接')
        connectButton.clicked.connect(self.connectAction)
        layout.addWidget(connectButton)
        self.setLayout(layout)

    def connectAction(self):
        """
        点击连接按钮之后的响应函数
        :return:
        """
        sshObject = SSH(self.addLine.text(),self.username.text(),self.password.text())
        sshSesson = sshObject.createSession()
        pathroot = sshObject.do_execution(sshSesson,'cd chen_guang_hao/PeDetect/smallcorgi/Faster-RCNN_TF-master/;pwd')








