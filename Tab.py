from PyQt5.QtWidgets import QTabWidget,QWidget,QLabel,QGridLayout,QRadioButton,QScrollBar,QVBoxLayout,QHBoxLayout
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
class Tab(QTabWidget):
    def __init__(self):
        super(Tab, self).__init__()
        print ('测试被调用了')
        tab1 = QWidget()
        tab2 = QWidget()
        self.addTab(tab1, "训练")
        self.addTab(tab2, "测试")

        tab2.setStyleSheet("background:black")

        #定义训练标签页的内容
        lay1 = QGridLayout()
        lay1.setSpacing(10)
        scroll_iter = QScrollBar(100)
        scroll_iter.setOrientation(QtCore.Qt.Horizontal)
        lay1.addWidget(QLabel('迭代次数'), 0, 0)
        lay1.addWidget(scroll_iter, 0, 1)
        lay1.addWidget(QRadioButton('是否有RPN'), 1, 0)
        scroll_Learn = QScrollBar(100)
        scroll_Learn.setOrientation(QtCore.Qt.Horizontal)
        lay1.addWidget(QLabel('学习率'), 2, 0)
        lay1.addWidget(scroll_Learn, 2, 1)
        image = QLabel()
        image.setScaledContents(True)
        resultPic = QPixmap('GPU.png')
        image.setPixmap(resultPic)
        lay1.addWidget(image,0,2,3,2)
        tab1.setLayout(lay1)


        # 定义训练标签页的内容
        lay2 = QGridLayout()
        #lay2.addWidget(label3)
        #lay2.addWidget(label4)
        tab2.setLayout(lay2)
    def testFunc(self):
        print ('testFunc')







