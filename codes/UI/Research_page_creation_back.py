import pandas
import Db_gestions as Db
import Autocompletion as autoc 
import Reasearch_page_creation_UI as RU
import back_recherche as br

dbs = Db.choix_db("Cocktail")


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
    for i in range(len(columns_names)):
        filtre =RU.Filtre(columns_names[i],columns_names[i])
        filters_list.append(filtre)
    for i in range(len(filters_list)):
        for j in range(filters_list[i].nb_elements):
            filters_list[i].name_edit_list[j].textEdited.connect(take_text)
    return filters_list


# Lis tout les QLineEdit qui font office de filtres et retourne tout leurs textes.
# Filtre la df en fonction des filtres utilisés et donne la df des éléments filtrés
def from_filters_to_newDF(df_used,filters_list,colonne_to_sort,sorted_state):
        df_temporary = df_used.copy()

        for i in range(len(filters_list)) :
            for j in range(len(filters_list[i].nb_elements)) :
                text_from_filter = filters_list[i].name_edit_list[j].text()
                if  text_from_filter != '':
                    
        
                    if df_temporary.dtypes[i] == type(1) :
                        df_temporary = br.filtrer((text_from_filter),filters_list[i].nom_col,df_temporary)

                    else :
                        df_temporary = br.filtrer(text_from_filter,filters_list[i].nom_col,df_temporary)
        

        df_temporary = df_temporary.sort_values(colonne_to_sort,ascending=sorted_state)
        return df_temporary


#Permet juste de choisir dans quelle sens on va tier 
def chose_sorted_sens(chosed_option):

        if chosed_option == "dsc" :
            return 'asc'
        else :
            return 'dsc'

    
    