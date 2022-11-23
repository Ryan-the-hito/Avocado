class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Thank you for your support!")

        buttons = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel('')

        m1 = QLabel('''
        Thank you for your kind support! 😊
        I will write more interesting apps! 🥳''', self)
        m1.move(10, 190)
        m1.resize(300, 60)

        l1 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('wechat_full.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l1.setGeometry(20, 20, 180, 200)
        l1.setScaledContents(True)

        l2 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('alipay_full.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l2.setGeometry(200, 20, 180, 200)
        l2.setScaledContents(True)

        self.resize(400, 300)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.center()

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())