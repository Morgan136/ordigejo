from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, \
    QPushButton, QToolBar, QCheckBox, QStatusBar, QGridLayout, QTextEdit
from PyQt6.QtGui import QAction, QIcon
import sys
from PyQt6.QtCore import Qt, QSize, QRect
import lorem
from datetime import datetime
import time

sortedList = [
    ["default_Name", "de Date", "el Источник", "priskribo " * 100],
    ["name1\nsecond string", "date1", "aux1", lorem.get_paragraph(5) + "КОНЕЦ КОНЕЦ КОНЕЦ"],
    ["name2", "date2", "aux2", "description2 " * 100],
    ["name3", str(datetime(1900, 12, 25, 13, 13)), "aux3", "description3 " * 100],
    ["name4", "de " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "aux4", "description4 " * 100],
]

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.width = 600
        self.height = 500

        self.setFixedSize(self.width, self.height)
        self.setWindowTitle("Ordigejo")

        self.n = 0

        # меню

        toolbar = QToolBar()
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        buttonImport = QAction(QIcon("bug.png"), "Импорт данных", self)
        buttonExport = QAction(QIcon("bug.png"), "Экспорт данных", self)
        buttonSource = QAction(QIcon("bug.png"), "Показать файл в Проводнике", self)

        buttonPreferencesDesign = QAction(QIcon("bug.png"), "Дизайн", self)
        buttonPreferencesImport = QAction(QIcon("bug.png"), "Импорт настроек", self)
        buttonPreferencesExport = QAction(QIcon("bug.png"), "Экспорт настроек", self)

        menu = self.menuBar()

        file_menu = menu.addMenu("File")
        file_menu.addAction(buttonImport)
        file_menu.addAction(buttonExport)
        file_menu.addAction(buttonSource)

        # подменю "Настройки"
        menuPreferences = file_menu.addMenu(QIcon("bug.png"), "Настройки")
        menuPreferences.addAction(buttonPreferencesDesign)
        menuPreferences.addAction(buttonPreferencesImport)
        menuPreferences.addAction(buttonPreferencesExport)

        self.setStatusBar(QStatusBar(self))

        # инициализация элементов

        # строка поиска
        self.elementSearch = QLineEdit()

        # контент

        # Имя
        self.elementName = QLabel(sortedList[0][0], self)

        # Описание
        self.elementDescription = QTextEdit(sortedList[0][3])
        self.elementDescription.setMaximumWidth(round(self.width * 0.75))
        self.elementDescription.setMaximumHeight(round(self.height * 1.85))

        # Дата
        self.elementDate = QLabel(sortedList[0][1])

        # Aux
        self.elementAux = QLabel(sortedList[0][2])

        # заглушка
        self.plug = QLabel()

        # кнопки
        self.nextButton = QPushButton("Next")
        self.nextButton.clicked.connect(self.nextElement)
        self.previousButton = QPushButton("Previous")
        self.previousButton.clicked.connect(self.previousElement)

        # добавление слоёв
        layoutMain = QGridLayout()
        layoutTop = QVBoxLayout()
        layoutBottom = QHBoxLayout()

        # добавление строки поиска
        layoutTop.addWidget(self.elementSearch)

        # добавление контента
        layoutMain.addWidget(self.elementName, 0, 0)
        layoutMain.addWidget(self.elementDescription, 1, 0)
        layoutMain.addWidget(self.plug, 0, 1)
        layoutMain.addWidget(self.plug, 0, 2)
        layoutMain.addWidget(self.elementDate, 0, 3)
        layoutMain.addWidget(self.elementAux, 1, 3)

        # добавление кнопок
        layoutBottom.addWidget(self.previousButton)
        layoutBottom.addWidget(self.nextButton)

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

        def mouseDoubleClickEvent(self, e):
            self.label.setText("mouseDoubleClickEvent")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
