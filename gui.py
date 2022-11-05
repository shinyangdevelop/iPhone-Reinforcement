import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from screeninfo import get_monitors


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iPhone Reinforcement")
        monitor = None
        for m in get_monitors():
            if m.is_primary:
                print(f'Monitor detected: {str(m)}')
                monitor = m
                break

        if monitor != None:
            print(str(m))
            self.resize(QSize(int(monitor.width/2), int(monitor.height/2)))

        #TODO: Make fixed ratio to 16:9, and look at https://forum.qt.io/topic/140533/fixing-the-ratio-of-width-and-height-in-the-qmainwindow-component-pyqt-6-4 


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)