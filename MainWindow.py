import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow,QLabel,QAction,QVBoxLayout,QTabWidget,QWidget,QFileDialog
from Tab import Tab
from UI.SSHDialog import SSHDialog
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # 中心部分
        self.resize(800,600)
        self.tab = Tab()
        self.setCentralWidget(self.tab)

        # 状态栏
        self.statusBar()

        # 菜单栏
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # 定义菜单：文件，连接，帮助
        fileMenu = menubar.addMenu("File")
        connectMenu = menubar.addMenu('Connect')
        helpMenu = menubar.addMenu('Help')

        # 文件菜单：导入图片，导出结果
        loadImageAction = QAction('导入图片', self)
        loadImageAction.setStatusTip('从本地导入一张图片用于测试')
        exportResultAction = QAction('导出结果',self)
        exportResultAction.setStatusTip('检测结果保存到本地')
        fileMenu.addAction(loadImageAction)
        fileMenu.addAction(exportResultAction)
        loadImageAction.triggered.connect(self.loadImageFunction)
        exportResultAction.triggered.connect(self.downloadImageFunction)

        # 连接菜单：连接服务器
        sshAction = QAction('连接服务器',self)
        sshAction.triggered.connect(self.sshFuntion)
        connectMenu.addAction(sshAction)

        #帮助菜单：帮助文档，版权
        helpDocAction = QAction('帮助文档',self)
        copyrightAction = QAction('版权', self)
        helpMenu.addAction(helpDocAction)
        helpMenu.addAction(copyrightAction)


        #  设置标题
        self.setWindowTitle("行人检测系统控制中枢")
    def sshFuntion(self):
        """
        点击连接服务器之后弹出对话框进行连接
        :return:
        """
        sshBox = SSHDialog()
        #当对话框关闭后显示状态信息
        if (sshBox.exec()):
            self.statusBar().showMessage(sshBox.getStatus())

    def loadImageFunction(self):
        """
        导入图片，显示在训练标签的原始图片中
        :return:
        """
        loadFileDia = QFileDialog()
        filename = loadFileDia.getOpenFileName(None,'选择图片','./')
        img = QPixmap(filename[0])
        img.scaled(self.tab.imageOriginLable.width(), self.tab.imageOriginLable.height(), Qt.IgnoreAspectRatio)
        self.tab.imageOriginLable.setPixmap(img)

    def downloadImageFunction(self):
        """
        从测试图片QLabel中导出结果，
        保存到根目录下面的picture/output中
        :return:
        """
        pass
