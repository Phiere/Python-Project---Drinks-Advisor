import sys
import typing
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureWidget
import matplotlib.pyplot as plt

class ScreenDescriptionWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Description Window")
    
        menuLayout = QHBoxLayout()
        descriptionLayout = QVBoxLayout()
        globalLayout = QHBoxLayout()

        boutonAcceuil = QPushButton('Home')
        boutonRetour = QPushButton('Back')
        boutonSettings = QPushButton('Settings')

        namelabel = QLabel('Name')
        descriptionLabel = QLabel('Description')

        menuLayout.addWidget(boutonAcceuil)
        menuLayout.addWidget(boutonRetour)
        menuLayout.addWidget(boutonSettings)

        descriptionLayout.addLayout(menuLayout)
        descriptionLayout.addWidget(namelabel)
        descriptionLayout.addWidget(descriptionLabel)

        imageitem = QLabel() 
        h = self.size().height()
        w = self.size().width()
        imageitem.setPixmap(QPixmap('bouteille.jpg').scaled(round(w/2),h))

        globalLayout.addLayout(descriptionLayout)
        globalLayout.addWidget(imageitem)

        self.setLayout(globalLayout)
        

class ScreenHomeWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Home Window")
        self.resize(1000,600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        globalLayout = QVBoxLayout()
        alccolLayout = QHBoxLayout()
        alcoolfreeLayout = QHBoxLayout()

        
        alcoolTitle = QLabel("alcool")
        alcoolTitle.setFrameStyle(QFrame.Box | QFrame.Plain)
        font = alcoolTitle.font()
        font.setBold(True)
        alcoolTitle.setFont(font)
        alcoolfreeTitle = QLabel("sans alcool")
        alcoolfreeTitle.setFrameStyle(QFrame.Box | QFrame.Plain)
        font = alcoolfreeTitle.font()
        font.setBold(True)
        alcoolfreeTitle.setFont(font)

        winebutton = QPushButton("Vin")
        winebutton.setSizePolicy(sizePolicy)
        beerbutton = QPushButton("Bière")
        beerbutton.setSizePolicy(sizePolicy)
        cocktailbutton = QPushButton("Cocktail")
        cocktailbutton.setSizePolicy(sizePolicy)

        coffebutton = QPushButton("Café")
        coffebutton.setSizePolicy(sizePolicy)
        theabutton = QPushButton("Thé")
        theabutton.setSizePolicy(sizePolicy)
        mocktailbutton = QPushButton("Mocktail")
        mocktailbutton.setSizePolicy(sizePolicy)

        alccolLayout.addWidget(winebutton)
        alccolLayout.addWidget(beerbutton)
        alccolLayout.addWidget(cocktailbutton)

        alcoolfreeLayout.addWidget(coffebutton)
        alcoolfreeLayout.addWidget(theabutton)
        alcoolfreeLayout.addWidget(mocktailbutton)

        globalLayout.addWidget(alcoolTitle)
        globalLayout.addLayout(alccolLayout)
        globalLayout.addWidget(alcoolfreeTitle)
        globalLayout.addLayout(alcoolfreeLayout)

        self.setLayout(globalLayout)



class MultiScreenApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Application multi-écrans")
        self.setGeometry(100, 100, 800, 600)  # Définissez la taille initiale de la fenêtre

        self.menu_bar = CustomMenuBar(self)
        
        # Définissez la barre de menu comme la barre de menu principale de la fenêtre
        self.setMenuBar(self.menu_bar)
        

        # Créez un widget empilable pour contenir plusieurs écrans
        self.stackedWidget = QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)

        # Créez des écrans (QWidget) et ajoutez-les au widget empilable
        screen1 = ScreenDescriptionWindow()

        menuLayout = QHBoxLayout()

        boutonAcceuil = QPushButton('Home')
        boutonRetour = QPushButton('Back')
        boutonSettings = QPushButton('Settings')

        menuLayout.addWidget(boutonAcceuil)
        menuLayout.addWidget(boutonRetour)
        menuLayout.addWidget(boutonSettings)

        homescreen = QStackedLayout()
        homescreen.addLayout(menuLayout)
        homescreen.addWidget(screen1)

        #screen1 = self.createScreen("Écran 1", "Cliquez sur le bouton pour passer à l'écran 2.", "Écran suivant", self.showScreen2)
        screen2 = ScreenHomeWindow()
        #screen2 = self.createScreen("Écran 2", "Cliquez sur le bouton pour passer à l'écran 1.", "Écran précédent", self.showScreen1)

        self.stackedWidget.addWidget(homescreen)
        self.stackedWidget.addWidget(screen2)

        # Affichez le premier écran
        self.stackedWidget.setCurrentIndex(0)

    def createScreen(self, title, message, buttonText, buttonAction):
        screen = QWidget()
        layout = QVBoxLayout()
        
        title_label = QPushButton(title)
        title_label.setStyleSheet("font-size: 20px;")
        layout.addWidget(title_label)

        message_label = QPushButton(message)
        layout.addWidget(message_label)

        button = QPushButton(buttonText)
        button.clicked.connect(buttonAction)
        layout.addWidget(button)

        screen.setLayout(layout)


        return screen

    def showScreen1(self):
        self.stackedWidget.setCurrentIndex(0)

    def showScreen2(self):
        self.stackedWidget.setCurrentIndex(1)

def main():
    app = QApplication(sys.argv)
    fenetre = MultiScreenApp()
    fenetre.show()
    app.exec()

if __name__ == '__main__':
    main()