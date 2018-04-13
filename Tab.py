from PyQt5.QtWidgets import QTableWidget,QWidget,QLabel,QVBoxLayout
class Tab(QTableWidget):
    def __int__(self):
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.addTab(self.tab1, "训练")
        self.addTab(self.tab2, "测试")

        self.label = QLabel("训练")

        #定义训练tab布局
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(self.label)
        self.tab1.setLayout(self.tab1.layout)

        # 定义训练tab布局
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(self.label)
        self.tab1.setLayout(self.tab1.layout)


