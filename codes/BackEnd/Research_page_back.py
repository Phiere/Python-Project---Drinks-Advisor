##############################
#Ce script contient les fonctions de back_end pour la création de l'écran Research. Toutes
#les fonctions crées ici seront utilisées dans le script : Research_page_UI.
##############################

import Db_gestions as Db
from PyQt5.QtWidgets import QWidget,QLineEdit,QCompleter
from PyQt5.QtCore import Qt
import random

class Autocompleter(QLineEdit):
    """Créer un widget d'automplétion pour les filtres dynamiques de l'écran de recherche
    
    - colonne : colonne de dataframe dont les éléments seront affichés en autocomplétion.
    """
    def __init__(self,colonne):
        super().__init__()
        self.lineEdit = QLineEdit()
        autocomplete_list = colonne.tolist()

        completer = QCompleter(autocomplete_list, self.lineEdit)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.lineEdit.setCompleter(completer)


class Filtre(QWidget):
    """Créer un LineEDit qui sera assemblé avec d'autres pour créer une liste de filtres dynamiques
    
    - name_column : colonne du data_frame auquel se réfère le filtre
    - data_base : data_base des éléments uniques choisis pour les filtres
    """
    def __init__(self,name_column,data_base) -> None:
        super().__init__()
        self.nom_col = name_column
        data_base = data_base.astype(str)
        autocompleter = Autocompleter(data_base)
        self.name_edit = autocompleter.lineEdit
        if self.nom_col in Db.list_elements :
            self.name_edit.setPlaceholderText(self.nom_col + " (if more than 1 split with ',')")
        else :
            self.name_edit.setPlaceholderText(self.nom_col)


def from_df_to_filters(take_text):
    """Construit la colonne des filtres dynamiques associée à la base de données choisie
    
    - take_text : fonction récupérant les textes de tous les différents filtres
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
        Db.research_length = len(df_temporary)
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


def chose_sorted_sens(chosed_option):
    """Change le sens de tri"""
    if chosed_option == "Ascending" :
        return 'Descending'
    else :
        return 'Ascending'
    

def filtrer(f, colonne, data_Frame):

    def convert_to_numeric(value):
        try:
            return float(value)
        except ValueError:
            return value

    #A commenter si on veut une recherche moins itérative, plus directe
    if not (colonne in Db.list_elements) :
        f = convert_to_numeric(f)
        tempdf = data_Frame[data_Frame[colonne] == f]
    
    else :
        f = f.split(",")
        tempdf = data_Frame.copy()
        for i in f:
            if i != "":
                i = convert_to_numeric(i)
                tempdf = tempdf[tempdf[colonne].apply(lambda x: i in x)]
        
    
    return tempdf


############################################################
# Test test concernant Autocompleter et Filtre sont visuels car ils dependant 
# de l'interface graphique, nous devons donc vérifier que :
# 1 - Lorsqu'on écrit dans un filtre des options déroulantes s'affiche en accord avec ce qui est écrit
# 2 - Lorsqu'on appuie sur entré en ayant navigué dans options avec les flèches cela complète le texte
# 3 - Les filtres correspondent aux colonnes de filtre des base de données et peuvent être remplis
# 4 - Il est possible de retoruver 10 boissons choisi aléatoirement grâce aux filtres dynamiques
############################################################
def test_chose_sorted_sens(chosed_option):
    print("test_chose_sorted_sens")
    chosed_option = 'Ascending'
    #Test 0:
    print("Test 0",'Descending' == chosed_option(chosed_option))
    #Test 1:
    chosed_option = 'Descending'
    print("Test 1", 'Ascending' == chosed_option(chosed_option))

if __name__ == '__main__':
    test = input("Tester les fonctions du script ? "+"\n"+"Attention les tests doivent être faits sur des bases de données non modifies (0/1) : ")
    if test : 
        test_chose_sorted_sens()
        test_filtrer()
    