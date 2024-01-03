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

class Autocompleter(QLineEdit):
    def __init__(self,colonne):
        super().__init__()


        self.lineEdit = QLineEdit()
        autocomplete_list = colonne.tolist()
        print(autocomplete_list)

        # Création d'un QCompleter avec la liste des suggestions
        completer = QCompleter(autocomplete_list, self.lineEdit)

        # Définir la casse (Qt.CaseInsensitive pour une recherche insensible à la casse)
        completer.setCaseSensitivity(Qt.CaseInsensitive)

        # Définir le QCompleter pour le QLineEdit
        self.lineEdit.setCompleter(completer)



####################################
# Test sur une fenetre vite
####################################

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
    
        layout = QVBoxLayout()    

        colonne_ingredients = cocktail['Ingredients']
        colonne_ingredients = colonne_ingredients.drop_duplicates()
        colonne_ingredients = colonne_ingredients.dropna()

        Autocompletion_line = Autocompleter(colonne_ingredients)
        layout.addWidget(Autocompletion_line)
        self.setLayout(layout)




if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

