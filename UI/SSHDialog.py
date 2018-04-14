#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import QApplication, QDialog,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton
from PyQt5 import QtCore
class SSHDialog(QDialog):
    def __init__(self):
        """
        构造函数
        """
        super(SSHDialog, self).__init__()
        self.initUI()
    def initUI(self):
        """
        定义界面
        :return:
        """
        self.setWindowTitle("SSH 连接")
        self.setGeometry(400, 400, 300, 260)
        layout = QVBoxLayout()
        row1Layout = QHBoxLayout()
        row1Layout.addWidget(QLabel('地址'))
        row1Layout.addWidget(QLineEdit())
        layout.addLayout(row1Layout)
        row2Layout = QHBoxLayout()
        row2Layout.addWidget(QLabel('端口'))
        row2Layout.addWidget(QLineEdit('22'))
        layout.addLayout(row2Layout)
        row4Layout = QHBoxLayout()
        row4Layout.addWidget(QLabel('用户名'))
        row4Layout.addWidget(QLineEdit())
        layout.addLayout(row4Layout)
        row3Layout = QHBoxLayout()
        row3Layout.addWidget(QLabel('密码'))
        passwdLine = QLineEdit()
        passwdLine.setEchoMode(QLineEdit.Password)
        row3Layout.addWidget(passwdLine)
        layout.addLayout(row3Layout)
        layout.addWidget(QPushButton('连接'))
        self.setLayout(layout)



