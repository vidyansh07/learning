import sys 
from PyQt5.QtWidgets import  QApplication, QMainWindow, QPushButton
from util.widget import Button, Text

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,600)
        button = Button("Click me to test", self)        
        button.setStyleSheet("background-color :red")
        button.clicked.connect(self.testing)
        button.move(499,40)
        
        text = Text("Hello", self, 24, "Gill Sans")
        text.move(100,40)
        
    def testing(self):
        print("Success")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())