############################################################
############################################################
############################################################
#DESCRIPTION
############################################################
############################################################
############################################################


import pandas
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Autocompleter(QLineEdit):
    def __init__(self,colonne):
        super().__init__()


        self.lineEdit = QLineEdit()
        autocomplete_list = colonne.tolist()
        #print(autocomplete_list)

        # Création d'un QCompleter avec la liste des suggestions
        completer = QCompleter(autocomplete_list, self.lineEdit)

        # Définir la casse (Qt.CaseInsensitive pour une recherche insensible à la casse)
        completer.setCaseSensitivity(Qt.CaseInsensitive)

        # Définir le QCompleter pour le QLineEdit
        self.lineEdit.setCompleter(completer)



############################################################
############################################################
############################################################
# Test 
############################################################
############################################################
############################################################

#Test sur les verres de la bdd cocktails. Peut être testé sur toutes les bases de données.
        
cocktail = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/cocktail_unique_elements.csv")
colonne_autocompleteur = cocktail['strGlass']
colonne_autocompleteur = colonne_autocompleteur.drop_duplicates()
colonne_autocompleteur = colonne_autocompleteur.dropna()
colonne_autocompleteur = colonne_autocompleteur.astype(str)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
    
        layout = QVBoxLayout()    
        Autocompletion_line = Autocompleter(colonne_ingredients)

        layout.addWidget(Autocompletion_line.lineEdit)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

