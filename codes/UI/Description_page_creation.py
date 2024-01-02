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

def main():
    app = QApplication(sys.argv)
    fenetre = ScreenDescriptionWindow()
    fenetre.show()
    app.exec()

if __name__ == '__main__':
    main()