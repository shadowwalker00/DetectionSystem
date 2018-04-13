import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow,QLabel,QAction
from  Tab import Tab
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # 中心部分
        self.train_tab = Tab(self)
        self.label = QLabel("显示一些内容")
        self.label.setMinimumSize(600, 500)
        self.label.setAlignment(Qt.AlignCenter)
        #self.setCentralWidget(self.la)

        # 状态栏
        self.statusBar()

        # 菜单栏
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # 定义菜单内容
        fileMenu = menubar.addMenu("File")

        # Action
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctr+Q')
        exitAction.setStatusTip('Exit Application')
        fileMenu.addAction(exitAction)

        #  设置标题
        self.setWindowTitle("行人检测系统控制中枢")


        """

    def openFile(self):
        self.label.setText("openAction is triggered")

    def quit(self):
        self.label.setText("quitAction is triggered")

    def setBold(self, isChecked):
        if isChecked:
            self.label.setText("boldAction is checked")
        else:
            self.label.setText("boldAction is not checked")

    def reset(self):
        self.label.setText("resetAction is triggered")

    def createAction(self, text, slot=None, shortcut=None,
            tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeperator()
            else:
                target.addAction(action)
                """
