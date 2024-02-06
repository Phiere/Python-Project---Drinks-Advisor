import pandas as pd
import Db_gestions as Db

def texte_vides(get_text):
    textes_recuperees,names = get_text()
    return all(s == "" for s in textes_recuperees)

def create_new_drink(get_text):
    data_base_index = Db.choix_de_la_data_base
    textes_recuperees,names = get_text()
   
    new_row = pd.Series() 
    Db.dbsall[data_base_index][0] = Db.dbsall[data_base_index][0]._append(new_row, ignore_index=True)

    new_index = len(Db.dbsall[data_base_index][0]) - 1
    Db.index_boisson = new_index

    for i in range(len(textes_recuperees)):
        texte = textes_recuperees[i]
        if texte == '' : texte = "Not renseigned yet"
        colonne = names[i]
        Db.dbsall[data_base_index][0].at[new_index,colonne] = texte

    Db.dbsall[data_base_index][0].at[new_index,'PersonalRating'] = 0
    Db.dbsall[data_base_index][0].at[new_index,'Favorite'] = 0
    add_uniques_element(get_text=get_text)


def add_uniques_element(get_text):
    textes_recuperees,names = get_text()
    data_base_index = Db.choix_de_la_data_base

    ## On rajoute toutes les nouvelles valeurs dans unique_element sans vérifier
    new_row = pd.Series() 
    Db.dbsall[data_base_index][1] = Db.dbsall[data_base_index][1]._append(new_row, ignore_index=True)
    new_index = len(Db.dbsall[data_base_index][1]) - 1      

    for i in range(len(textes_recuperees)) :
        texte = textes_recuperees[i]
        colonne = names[i]
        Db.dbsall[Db.choix_de_la_data_base][1].at[new_index,colonne] = texte
    
    uniques_elements_columns_list = []

    for name in Db.dbsall[Db.choix_de_la_data_base][1].columns :
        uniques_elements_column = Db.dbsall[Db.choix_de_la_data_base][1][name].drop_duplicates()
        uniques_elements_columns_list.append(uniques_elements_column)


    new_unique_element = pd.DataFrame(dict(zip(Db.dbsall[Db.choix_de_la_data_base][1].columns,uniques_elements_columns_list)))
    Db.dbsall[Db.choix_de_la_data_base][1] = new_unique_element




