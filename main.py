import sys
import random
from PyQt6.QtWidgets import *
from iPhone import Iphone_Reinforcement
from gui import MainWindow

if __name__ == "__main__":
    App = Iphone_Reinforcement()

    gui = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    gui.exec()
    # #Initialize
    # print(f"current: {App.iPhones[App.current][0]}")
    # print(f"chance: {App.iPhones[App.current][2] * 100}%")
    
    # while True:
    #     command = str(input())
    #     if command == "ir close":
    #         sys.exit(0)
    #     else:
    #         App.Commanding(command)
