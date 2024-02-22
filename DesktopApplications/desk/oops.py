import sys
from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox,QPushButton

class App:
    def __init__(self):
        self.app = QApplication(sys.argv) # Ignore
        self.windows = QWidget()
        self.massage = QMessageBox()
        self.button = QPushButton()

    def screen(self):
        self.windows.setGeometry(0,0,800,500)
        self.windows.setWindowTitle("Name") 
        self.windows.setStyleSheet("background-color : orange")
        self.windows.show()
        
    def handleMinimize(self):
        self.windows.showMinimized()

    def handleMaximize(self):
        self.windows.showMaximized()

    def handleClose(self):
        self.windows.close()

        self.minButton =QPushButton("Minimize",self.windows)
        self.minButton.setStyleSheet("background-color : white")
        self.minButton.move(40, 60)
        self.minButton.clicked.connect(self.handleMinimize)

        self.maxButton= QPushButton("Maximize",self.windows)
        self.maxButton.setStyleSheet("background-color : white")
        self.maxButton.move(150, 60)
        self.maxButton.clicked.connect(self.handleMaximize)

        self.clButton= QPushButton("Close",self.windows)
        self.clButton.setStyleSheet("background-color : white")
        self.clButton.move(260, 60)
        self.clButton.clicked.connect(self.handleClose)


    
        
app = App()
app.screen()
sys.exit(app.exec_())