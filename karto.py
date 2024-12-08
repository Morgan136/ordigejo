from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout
import time
from PyQt6.QtCore import Qt
import random

from qwt.legend import buttonShift

list1 = [
    "dsadad10",
    "dsadad9",
    "dsadad8",
    "dsadad7",
    "dsadad6",
    "dsadad5",
    "dsadad4",
    "dsadad3",
    "dsadad2",
    "dsadad1"
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel(random.choice(list1))
        self.button = QPushButton("b for text")
        self.input = QLineEdit()

        self.input.textChanged.connect(self.button.setText)
        self.button.clicked.connect(self.label_change)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button, alignment = Qt.AlignmentFlag.AlignRight)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def label_change(self):
        self.label.setText(random.choice(list1))

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
