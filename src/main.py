import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QVBoxLayout, QLineEdit, QGridLayout, QGroupBox, QCalendarWidget, QListWidget, QPlainTextEdit
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
        
        mainLayout = QGridLayout()
        mainBox.setLayout(mainLayout)
        
        calendarBox = QGroupBox("Events")
        calendarLayout = QGridLayout()
        calendar = QCalendarWidget()
        calendarLayout1 = QGridLayout()
        calendarLayout1.addWidget(calendar)
        calendarBox1 = QGroupBox("Calendar")
        calendarBox1.setLayout(calendarLayout1)
        calendarList = QListWidget()
        calendarEventInfo = QLabel("Event Description")
        calendarEventDescription = QPlainTextEdit()
        calendarList.addItems(["Event1", "Event2"])
        calendarLayout.addWidget(calendarList, 1, 3)
        calendarLayout.addWidget(calendarBox1, 1, 1)
        calendarLayout.addWidget(calendarEventInfo, 2, 3)
        calendarLayout.addWidget(calendarEventDescription, 3, 3)
        calendarBox.setLayout(calendarLayout)
        mainLayout.addWidget(calendarBox, 1, 1)
        
        
        

        
        widget.setLayout(baseLayout)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(1000, 500))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()