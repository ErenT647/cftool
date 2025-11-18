import argparse
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtQml import QQmlApplicationEngine
import random

class Window(QWidget):
    def __init__(self):
        super().__init__()

    def add_node():
        pass
    

app = QApplication(sys.argv)
engine = QQmlApplicationEngine()
window = Window()
engine.rootContext().setContextProperty('window', window)
engine.load('graph.qml')
sys.exit(app.exec())
