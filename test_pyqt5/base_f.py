import sys
from PyQt5.QtWidgets import QApplication, QWidget
from time import sleep

app = QApplication(sys.argv)
w = QWidget()
w.resize(300, 200)
w.move(100, 100)
w.setWindowTitle('hello')
w.show()

sleep(10)