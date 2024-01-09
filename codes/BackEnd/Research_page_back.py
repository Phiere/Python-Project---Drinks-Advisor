import Db_gestions as Db
import Autocompletion as autoc 
from PyQt5.QtWidgets import QWidget

dbs = Db.choix_db("Cocktail")

class Filtre(QWidget):
    def __init__(self,name_column,displayed_text) -> None:
        super().__init__()
        self.nom_col = name_column
        autocompleter = from_name_to_unique_elements_completer(name_column)
        self.name_edit = autocompleter.lineEdit
        self.name_edit.setPlaceholderText(displayed_text)

## Se charge de créer le completeur qui servira pour l'autocomplétion sur un QLineEdit
## On prend seulement en entrée la colonne dont on veut les éléments de complétion

def from_name_to_unique_elements_completer(name_column):
    colonne_unique_elements = dbs[2][name_column]
    colonne_unique_elements = colonne_unique_elements.drop_duplicates()
    colonne_unique_elements = colonne_unique_elements.dropna()
    colonne_unique_elements = colonne_unique_elements.astype(str)
    return autoc.Autocompleter(colonne_unique_elements)


# Prend en entrée la df utilisée et construit une list de filtres qui seront utililisés à la
# fois pour l'affichage et la gestion des données à afficher

def from_df_to_filters(df_used,take_text):
    columns_names = df_used.columns 
    filters_list = []
    for i in range(1,len(columns_names)):
        filtre = Filtre(columns_names[i],columns_names[i])
        filters_list.append(filtre)
    for i in range(len(filters_list)):
            filters_list[i].name_edit.textEdited.connect(take_text)
    return filters_list


# Lis tout les QLineEdit qui font office de filtres et retourne tout leurs textes.
# Filtre la df en fonction des filtres utilisés et donne la df des éléments filtrés
def from_filters_to_newDF(df_used,filters_list,colonne_to_sort,sorted_state):
        df_temporary = df_used.copy()

        for i in range(len(filters_list)) :
                text_from_filter = filters_list[i].name_edit.text()
                if  text_from_filter != '':
                    
                    df_temporary = filtrer(text_from_filter,filters_list[i].nom_col,df_temporary)
        

        #df_temporary = df_temporary.sort_values(colonne_to_sort,ascending=sorted_state)
        
        return df_temporary[dbs[3]]


#Permet juste de choisir dans quelle sens on va trier 
def chose_sorted_sens(chosed_option):

        if chosed_option == "dsc" :
            return 'asc'
        else :
            return 'dsc'

    
    #Filtre les databases sur une colone donée avec un filtre précis

def filtrer(f,colonne,data_Frame):
    try:
        int(f)
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
            
        return tempdf

#Retourne les noms des colonnes de la bdd chargée ainsi que les types des colonnes (utile pour les comparaisons)
def colonnes(data_Frame):
    columns = data_Frame.columns
    types = data_Frame.dtypes
    L = []
    for i in range(len(colonnes)):
        L.append([columns[i],types[i]])
    return L