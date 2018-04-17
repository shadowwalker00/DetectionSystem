from PyQt5.QtWidgets import QTabWidget,QWidget,QLabel,QRadioButton,QScrollBar,QVBoxLayout,QHBoxLayout,QTextEdit,QFormLayout,QPushButton
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
class Tab(QTabWidget):
    def __init__(self):
        super(Tab, self).__init__()
        tab1 = QWidget()
        tab2 = QWidget()
        self.addTab(tab1, "训练")
        self.addTab(tab2, "测试")

        #定义训练标签页的内容
        lay1 = QHBoxLayout()
        lay1.setSpacing(20)
        formLay = QFormLayout()            #定义左侧表单layout
        #设置Formlay的样式
        formLay.setLabelAlignment(QtCore.Qt.AlignLeft)
        formLay.setFormAlignment(QtCore.Qt.AlignCenter)
        formLay.setVerticalSpacing(50)
        lefttitle = QLabel('训练参数设置面板')
        lefttitle.setAlignment(QtCore.Qt.AlignHCenter)
        formLay.addRow(lefttitle)
        scroll_iter = QScrollBar()      #迭代次数的滚动条
        scroll_iter.setMinimumWidth(100)
        scroll_iter.setOrientation(QtCore.Qt.Horizontal)
        formLay.addRow("迭代次数",scroll_iter)
        formLay.addRow("是否使用RPN",QRadioButton())
        scroll_Learn = QScrollBar()     #学习率滚动条
        scroll_Learn.setMinimumWidth(100)
        scroll_Learn.setOrientation(QtCore.Qt.Horizontal)
        formLay.addRow('学习率', scroll_Learn)
        train_button = QPushButton('开始训练')
        formLay.addRow(train_button)
        train_button.clicked.connect(self.train)
        lay1.addLayout(formLay)
        lay1.setStretchFactor(formLay, 1)    #定义左侧的FormLayout占据整个的1/3

        #设置右侧结果VLayout
        resultLay = QVBoxLayout()
        rightTitle = QLabel('训练结果显示面板')
        rightTitle.setAlignment(QtCore.Qt.AlignHCenter)
        resultLay.addWidget(rightTitle)
        self.imageLable1 = QLabel()
        self.imageLable1.setFixedHeight(self.height()/2)
        self.imageLable1.setFixedWidth(self.width()/3*2)
        resultLay.addWidget(self.imageLable1)
        resultLay.addWidget(QTextEdit())
        lay1.addLayout(resultLay)
        lay1.setStretchFactor(resultLay, 2)
        tab1.setLayout(lay1)

        # 定义测试标签页的内容
        lay2 = QHBoxLayout()
        #原始图片Label
        layLeft = QVBoxLayout()
        originTitle = QLabel('原始图片')
        originTitle.setAlignment(QtCore.Qt.AlignHCenter)
        layLeft.addWidget(originTitle)
        self.imageOriginLable = QLabel()
        self.imageOriginLable.setAlignment(QtCore.Qt.AlignCenter)
        self.imageOriginLable.setFixedWidth(self.width() / 2)
        self.imageOriginLable.setFixedHeight(self.height())
        layLeft.addWidget(self.imageOriginLable)

        #测试图片Label
        layRight = QVBoxLayout()
        detectTitle = QLabel('检测结果')
        detectTitle.setAlignment(QtCore.Qt.AlignHCenter)
        layRight.addWidget(detectTitle)
        self.imageDetectLable = QLabel()
        self.imageDetectLable.setAlignment(QtCore.Qt.AlignCenter)
        self.imageDetectLable.setFixedWidth(self.width() / 2)
        self.imageDetectLable.setFixedHeight(self.height())
        layRight.addWidget(self.imageDetectLable)

        lay2.addLayout(layLeft)
        lay2.addLayout(layRight)
        tab2.setLayout(lay2)

    def train(self):
        """
        执行训练函数
        :return:
        """
        print('开始训练')
        pass






