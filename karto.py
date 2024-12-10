from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, \
    QPushButton, QToolBar, QCheckBox, QStatusBar, QGridLayout
from PyQt6.QtGui import QAction, QIcon
import sys
from PyQt6.QtCore import Qt, QSize

sortedList = [
    ["defaultName", "defaultDate", "defaultAux", "defaultDescription"],
    ["name1", "date1", "aux1", "description1"],
    ["name2", "date2", "aux2", "description2"],
    ["name3", "date3", "aux3", "description3"],
    ["name4", "date4", "aux4", "description4"]
]

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)

        self.setWindowTitle("Ordigejo")

        self.n = 0

        # меню

        toolbar = QToolBar()
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        #toolbar.addSeparator()

        button_action = QAction(QIcon("bug.png"), "Кнопка 1", self)
        button_action2 = QAction(QIcon("bug.png"), "Кнопка 2", self)

        menu = self.menuBar()

        file_menu = menu.addMenu("File")
        file_menu.addAction(button_action)
        file_menu.addAction(button_action2)

        self.setStatusBar(QStatusBar(self))

        # инициализация элементов

        # строка поиска
        self.elementSearch = QLineEdit()

        # элементы для левой части
        self.elementName = QLabel(sortedList[0][0]) # Имя
        self.elementDescription = QLabel(sortedList[0][3]) # Описание

        # элементы для правой части
        self.elementDate = QLabel(sortedList[0][1]) # Дата
        self.elementAux = QLabel(sortedList[0][2]) # Aux

        # кнопки
        self.nextButton = QPushButton("Next")
        self.nextButton.clicked.connect(self.nextElement)
        self.previousButton = QPushButton("Previous")
        self.previousButton.clicked.connect(self.previousElement)

        #layoutMain.addLayout(layoutLeft) # добавление левой части: Имя, Описание
        #layoutMain.addLayout(layoutRight) # добавление правой части: Дата, Aux
        #layoutMain.addLayout(layoutControl) # добавление кнопок

        # добавление слоёв
        layoutMain = QGridLayout()
        layoutTop = QVBoxLayout()
        layoutBottom = QHBoxLayout()

        # добавление строки поиска
        layoutTop.addWidget(self.elementSearch)

        # добавление контента
        layoutMain.addWidget(self.elementName, 0, 0)
        layoutMain.addWidget(self.elementDescription, 1, 0)
        layoutMain.addWidget(self.elementDate, 0, 1)
        layoutMain.addWidget(self.elementAux, 1, 1)

        # добавление кнопок
        layoutBottom.addWidget(self.nextButton)
        layoutBottom.addWidget(self.previousButton)

        layoutTop.addLayout(layoutMain)
        layoutTop.addLayout(layoutBottom)

        container = QWidget()
        container.setLayout(layoutTop)
        self.setCentralWidget(container)

    def nextElement(self):
        self.n += 1

        try:
            self.elementName.setText(sortedList[self.n][0])
            self.elementDate.setText(sortedList[self.n][1])
            self.elementAux.setText(sortedList[self.n][2])
            self.elementDescription.setText(sortedList[self.n][3])
        except IndexError:
            self.n = 0
            self.elementName.setText(sortedList[self.n][0])
            self.elementDate.setText(sortedList[self.n][1])
            self.elementAux.setText(sortedList[self.n][2])
            self.elementDescription.setText(sortedList[self.n][3])

    def previousElement(self):
        self.n -= 1

        try:
            self.elementName.setText(sortedList[self.n][0])
            self.elementDate.setText(sortedList[self.n][1])
            self.elementAux.setText(sortedList[self.n][2])
            self.elementDescription.setText(sortedList[self.n][3])
        except IndexError:
            self.n = len(sortedList) - 1
            self.elementName.setText(sortedList[self.n][0])
            self.elementDate.setText(sortedList[self.n][1])
            self.elementAux.setText(sortedList[self.n][2])
            self.elementDescription.setText(sortedList[self.n][3])

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
