from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys
import functions

WIDTH = 600
HEIGHT = 300

def create_plus_buttom(window, pos, func=None):
    b1 = QtWidgets.QPushButton(window)
    b1.setText("+")
    b1.setMaximumSize(20, 20)
    b1.move(pos[0], pos[1])
    try:
        b1.clicked.connect(func)
    except:
        pass
    return b1

def create_folder_label(window, pos, text):
    l1 = QtWidgets.QLabel(window)
    l1.setText(text)
    l1.setMinimumSize(100, 50)
    l1.setMaximumSize(100, 50)
    l1.move(pos[0], pos[1])

def create_buttoms(win):
    dicc = functions.lector()
    i = 50
    for key, _ in dicc.items():
        b = create_plus_buttom(win, (50, i), event)
        create_folder_label(win, (100, i-15), key)
        i+=50

buttom_list = []

def event():
    print("Clicked")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry((1920 - WIDTH) / 2, (1080 - HEIGHT) / 2, WIDTH, HEIGHT)
    win.setWindowTitle("Download Handler")
    create_buttoms(win)


    win.show()
    sys.exit(app.exec_())

window()