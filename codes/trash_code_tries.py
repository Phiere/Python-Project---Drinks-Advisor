############################################################
############################################################
############################################################
# c'est ma poubelle les codes la servent à rien.

############################################################
############################################################
############################################################
import pandas as pd
import csv
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QLineEdit, QHBoxLayout


class CustomListItem(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)

        # Créer quatre zones de texte
        self.lineEdits = [QLineEdit(self) for _ in range(4)]
        for lineEdit in self.lineEdits:
            layout.addWidget(lineEdit)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(900,700)
        layout = QVBoxLayout(self)

        # Créer le QListWidget
        self.listWidget = QListWidget()
        layout.addWidget(self.listWidget)

        # Ajouter des éléments personnalisés à QListWidget
        for i in range(10):  # Exemple avec 10 éléments
            listItem = QListWidgetItem(self.listWidget)
            customItemWidget = CustomListItem()
            listItem.setSizeHint(customItemWidget.sizeHint())
            self.listWidget.addItem(listItem)
            self.listWidget.setItemWidget(listItem, customItemWidget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

