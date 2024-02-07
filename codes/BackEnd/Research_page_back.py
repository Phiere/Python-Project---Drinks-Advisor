import Db_gestions as Db
from PyQt5.QtWidgets import QWidget,QLineEdit,QCompleter
from PyQt5.QtCore import Qt
import random
import pandas as pd

dbs = Db.initilisationSoft()[0]

#V0.1
class Autocompleter(QLineEdit):
    """Créer un widget d'automplétion pour les filtres dynamiques de l'écran de recherche
    
    - colonne : colonen de dataframe dont les éléments seront affichés en autocomplétion.
    """
    def __init__(self,colonne):
        super().__init__()
        self.lineEdit = QLineEdit()
        autocomplete_list = colonne.tolist()
        completer = QCompleter(autocomplete_list, self.lineEdit)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.lineEdit.setCompleter(completer)

#V0.1
class Filtre(QWidget):
    """Créer un LineEDit qui sera assemblé avec d'autres pour créer une liste de filtres dynamiques
    
    - name_column : colonne du data_frame auquel se refaire le filtre
    - data_base : data_base des éléments uniques choisie pour les filtres
    """
    def __init__(self,name_column,data_base) -> None:
        super().__init__()
        self.nom_col = name_column
        data_base = data_base.astype(str)
        autocompleter = Autocompleter(data_base)
        self.name_edit = autocompleter.lineEdit
        self.name_edit.setPlaceholderText(self.nom_col)

#v0.1
def from_df_to_filters(take_text):
    """Construit la colonne des filtres dynamiques associée à la base de données choisie
    
    - take_text : fonction récupérant les textes de tous les différents filtre
    - filters_list : liste des filtres à afficher sur l'écran recherche"""
    data_fram_unique_element = Db.dbsall[Db.choix_de_la_data_base][1]
    columns_names = data_fram_unique_element.columns
    filters_list = []
    for i in range(len(columns_names)):
        filtre = Filtre(columns_names[i],data_fram_unique_element.iloc[:,i])
        filters_list.append(filtre)
    for i in range(len(filters_list)):
            filters_list[i].name_edit.textEdited.connect(take_text)
    return filters_list

#v0.05
def from_filters_to_newDF(filters_list,number_of_element,colonne_to_sort,sorted_state):
        """Lis tout les QLineEdit qui font office de filtres et retourne tout leurs textes. Filtre la df en fonction des filtres utilisés et donne la df des éléments filtrés

        - filters_list : fourni la liste des filtres présent sur l'écran de rercherche
        - number_of_element : nombre d'éléments du data_frame à afficher sur l'écran
        - colonne_to_sort : colonne sur laquelle le tri sera fait
        - sorted_state : choisit le sens de tri selon lequel les données seront affichées 
        """
        df_used = Db.dbsall[Db.choix_de_la_data_base][0]
        df_temporary = df_used.copy()

        for i in range(len(filters_list)) :
                text_from_filter = filters_list[i].name_edit.text()
                if  text_from_filter != '':
          
                    df_temporary = filtrer(text_from_filter,filters_list[i].nom_col,df_temporary)
        

        if colonne_to_sort != 'Random':
            df_temporary = df_temporary.sort_values(colonne_to_sort,ascending=sorted_state)

        n = int(number_of_element)
        
        if not(df_temporary.empty) and len(df_temporary) > n:
            if colonne_to_sort == 'Random':
                L = random.sample(range(len(df_temporary)), n)
            else :   
                L = range(0,n)
        else :
            L = range(len(df_temporary))
        
        indexes = []
        
        for i in L:
             index = df_temporary.iloc[[i]].index[0]
             indexes.append(index)
   

        data_frame = Db.dbsall[Db.choix_de_la_data_base][0]
        colonne_interessantes = Db.dbsall[Db.choix_de_la_data_base][2]
        textes = []

        for i in (indexes):
            texte = [str(data_frame.at[i,j]) for j in colonne_interessantes]
            textes.append(texte)
            

        return indexes,L,textes

#v0.1
def chose_sorted_sens(chosed_option):
    """Change le sens de tri"""
    if chosed_option == "Ascending" :
        return 'Descending'
    else :
        return 'Ascending'
    
#v0.0
def filtrer(f, colonne, data_Frame):
    def extract_elements_from_list(value_str):
        value_str = str(value_str)  # Convertir en chaîne de caractères
        if value_str.startswith('[') and value_str.endswith(']'):
            value_list = [item.strip("' ") for item in value_str[1:-1].split(',')]
            seen_elements = set()
            value_list_filtered = [item for item in value_list if item != 'Unfilled' and item != '' and item != ' ' and (item not in seen_elements and seen_elements.add(item) is None)]
            return value_list_filtered
        else:
            return [value_str]

    def convert_to_numeric(value):
        try:
            return float(value)
        except ValueError:
            return value

    if "," not in f:
        tempdf = data_Frame[data_Frame[colonne].apply(lambda x: convert_to_numeric(f) in map(convert_to_numeric, extract_elements_from_list(x)))]
    else:
        f = f.split(",")
        tempdf = data_Frame.copy()
        for i in f:
            if i != "":
                tempdf = tempdf[tempdf[colonne].apply(lambda liste: convert_to_numeric(i) in map(convert_to_numeric, extract_elements_from_list(liste)))]

    return tempdf

############################################################
############################################################
############################################################
# Test 
############################################################
############################################################
############################################################

"""
cocktail = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/cocktail_unique_elements.csv")
colonne_autocompleteur = cocktail['strGlass']
colonne_autocompleteur = colonne_autocompleteur.drop_duplicates()
colonne_autocompleteur = colonne_autocompleteur.dropna()
colonne_autocompleteur = colonne_autocompleteur.astype(str)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
    
        layout = QVBoxLayout()    
        Autocompletion_line = Autocompleter(colonne_autocompleteur)

        layout.addWidget(Autocompletion_line.lineEdit)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
"""
