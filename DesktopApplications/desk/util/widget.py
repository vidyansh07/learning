from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QFont

def Button(text,window):
    return QPushButton(text, window)

def Text(text, window, size, family):
    label = QLabel(text, window)
    font = QFont( family,size)
    label.setFont(font)
    label.adjustSize()
    return label

