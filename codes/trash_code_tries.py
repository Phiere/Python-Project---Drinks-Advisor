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


cocktail = pd.read_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/cocktail_unique_elements.csv")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Création d'un QLineEdit
        self.lineEdit = QLineEdit(self)

        # Utilisation de la colonne 'Fruits' comme liste d'autocomplétion
        colonne_ingredients = cocktail['Ingredients']
        colonne_ingredients = colonne_ingredients.drop_duplicates()
        colonne_ingredients = colonne_ingredients.dropna()
        autocomplete_list = colonne_ingredients.tolist()
        print(autocomplete_list)
        # Création d'un QCompleter avec la liste des suggestions
        completer = QCompleter(autocomplete_list, self.lineEdit)

        # Définir la casse (Qt.CaseInsensitive pour une recherche insensible à la casse)
        completer.setCaseSensitivity(Qt.CaseInsensitive)

        # Définir le QCompleter pour le QLineEdit
        self.lineEdit.setCompleter(completer)

        # Ajout du QLineEdit au layout
        layout.addWidget(self.lineEdit)

        # Affichage de la fenêtre
        self.setLayout(layout)
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()

