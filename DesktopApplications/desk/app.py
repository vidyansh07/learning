import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox

app = QApplication(sys.argv)
window = QWidget()
massage = QMessageBox()

def handleMinimize():
    window.showMinimized()

def handleMaximize():
    window.showMaximized()

def handleClose():
    window.close()

minButton =QPushButton("Minimize",window)
minButton.setStyleSheet("background-color : white")
minButton.move(40, 60)
minButton.clicked.connect(handleMinimize)

maxButton= QPushButton("Maximize",window)
maxButton.setStyleSheet("background-color : white")
maxButton.move(150, 60)
maxButton.clicked.connect(handleMaximize)

clButton= QPushButton("Close",window)
clButton.setStyleSheet("background-color : white")
clButton.move(260, 60)
clButton.clicked.connect(handleClose)

window.setGeometry(0,0,800,500)
window.setWindowTitle("Name") 
window.setStyleSheet("background-color : orange")
window.show()

sys.exit(app.exec_())