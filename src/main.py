import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QVBoxLayout, QLineEdit, QGridLayout, QGroupBox
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Caster")
        widget = QWidget()
        mainBox = QGroupBox("Hub")

        baseLayout = QGridLayout()
        baseLayout.addWidget(mainBox, 0, 0)
        
        mainBox.setLayout(baseLayout)


        eventsLayout = QGridLayout()
        eventsBox = QGroupBox()

        eventsBox.setLayout(eventsLayout)

        Text = QLineEdit()

        eventsLayout.addWidget(Text)

        
        widget.setLayout(baseLayout)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(1000, 500))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()