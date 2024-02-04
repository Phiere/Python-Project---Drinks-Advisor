import Db_gestions as Db
import Autocompletion as autoc 
from PyQt5.QtWidgets import QWidget
import random
import pandas as pd

dbs = Db.initilisationSoft()[0]


class Filtre(QWidget):
    def __init__(self,name_column,data_base) -> None:
        super().__init__()
        self.nom_col = name_column
        data_base = data_base.astype(str)
        autocompleter = autoc.Autocompleter(data_base)
        self.name_edit = autocompleter.lineEdit
        self.name_edit.setPlaceholderText(self.nom_col)


# Prend en entrée la df utilisée et construit une list de filtres qui seront utililisés à la
# fois pour l'affichage et la gestion des données à afficher
# je change pas la db ici oups
def from_df_to_filters(take_text):
    db = Db.dbsall[Db.choix_de_la_data_base][1]
    columns_names = db.columns
    filters_list = []
    for i in range(len(columns_names)):
        filtre = Filtre(columns_names[i],db.iloc[:,i])
        filters_list.append(filtre)
    for i in range(len(filters_list)):
            filters_list[i].name_edit.textEdited.connect(take_text)
    return filters_list


# Lis tout les QLineEdit qui font office de filtres et retourne tout leurs textes.
# Filtre la df en fonction des filtres utilisés et donne la df des éléments filtrés
def from_filters_to_newDF(filters_list,number_of_element,colonne_to_sort,sorted_state):
        df_used = Db.dbsall[Db.choix_de_la_data_base][0]
        df_temporary = df_used.copy()

        for i in range(len(filters_list)) :
                text_from_filter = filters_list[i].name_edit.text()
                if  text_from_filter != '':
          
                    df_temporary = filtrer(text_from_filter,filters_list[i].nom_col,df_temporary)
        

        if colonne_to_sort != 'Random':
            if Db.choix_de_la_data_base == 0 and colonne_to_sort == 'Price':
                df_temporary[colonne_to_sort] = pd.to_numeric(df_temporary[colonne_to_sort], errors='coerce')
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
        print(indexes)

        data_frame = Db.dbsall[Db.choix_de_la_data_base][0]
        colonne_interessantes = Db.dbsall[Db.choix_de_la_data_base][2]
        textes = []

        for i in (indexes):
            texte = [str(data_frame.at[i,j]) for j in colonne_interessantes]
            textes.append(texte)
            

        return indexes,L,textes


#Permet juste de choisir dans quel sens on va trier 
def chose_sorted_sens(chosed_option):

        if chosed_option == "Ascending" :
            return 'Descending'
        else :
            return 'Ascending'

    
#Filtre les databases sur une colonne donnée avec un (ou des) filtre(s) précis
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

    """try:
        1==0#int(f)
        return data_Frame[data_Frame[colonne] == int(f)]
    except ValueError :    
        if "," not in f :
            return data_Frame[data_Frame[colonne] == f]
        else :
            f = f.split(",")
            tempdf = data_Frame.copy()
            for i in f :
                if i != "" :
                    tempdf = tempdf[tempdf[colonne].apply(lambda liste: i in liste)]
        
        tempdf = tempdf.reset_index().rename(columns={'index': 'Ancien_Index'})
        print("pouqoi j'ai")
        print(tempdf.head(5))
        return tempdf"""

#Retourne les noms des colonnes de la bdd chargée ainsi que les types des colonnes (utile pour les comparaisons)
def colonnes(data_Frame):
    columns = data_Frame.columns
    types = data_Frame.dtypes
    L = []
    for i in range(len(colonnes)):
        L.append([columns[i],types[i]])
    return L