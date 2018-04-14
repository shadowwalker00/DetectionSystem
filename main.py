#!/user/bin/python3
#-*- coding:utf-8 -*-

'''
Creat a simple window
'''
__author__ = 'Guanghao Chen'

import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainW = MainWindow()
    mainW.show()
    sys.exit(app.exec_())