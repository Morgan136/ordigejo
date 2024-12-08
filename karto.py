from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton
import sys
from PyQt6.QtCore import Qt

sortedList = [
    ["defaultName", "defaultDate", "defaultAux"],
    ["name1", "date1", "aux1"],
    ["name2", "date2", "aux2"],
    ["name3", "date3", "aux3"],
    ["name4", "date4", "aux4"]
]

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ordigejo")

        self.n = 0

        self.elementName = QLabel(sortedList[0][0])
        self.elementDate = QLabel(sortedList[0][1])
        self.elementAux = QLabel(sortedList[0][2])

        self.nextButton = QPushButton("Next")
        self.nextButton.clicked.connect(self.nextElement)

        self.previousButton = QPushButton("Previous")
        self.previousButton.clicked.connect(self.previousElement)

        layout = QVBoxLayout()
        layout.addWidget(self.elementName)
        layout.addWidget(self.elementDate)
        layout.addWidget(self.elementAux)
        layout.addWidget(self.nextButton, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.previousButton, alignment=Qt.AlignmentFlag.AlignLeft)



        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def nextElement(self):
        self.n += 1

        try:
            self.elementName.setText(sortedList[self.n][0])
            self.elementDate.setText(sortedList[self.n][1])
            self.elementAux.setText(sortedList[self.n][2])
        except IndexError:
            self.n = 0
            self.elementName.setText(sortedList[self.n][0])
            self.elementDate.setText(sortedList[self.n][1])
            self.elementAux.setText(sortedList[self.n][2])


    def previousElement(self):
        self.n -= 1

        try:
            self.elementName.setText(sortedList[self.n][0])
            self.elementDate.setText(sortedList[self.n][1])
            self.elementAux.setText(sortedList[self.n][2])
        except IndexError:
            self.n = len(sortedList) - 1
            self.elementName.setText(sortedList[self.n][0])
            self.elementDate.setText(sortedList[self.n][1])
            self.elementAux.setText(sortedList[self.n][2])


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
