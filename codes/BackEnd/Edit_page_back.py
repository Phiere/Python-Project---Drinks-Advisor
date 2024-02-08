import pandas as pd
import Db_gestions as Db
from PyQt5.QtWidgets import QMessageBox

def texte_vides(get_text):
    textes_recuperees,_ = get_text()
    strInvalid = []
    numberInvalid = []
    for i,texte in enumerate(textes_recuperees) :
        if texte == 'numberFalse':
            numberInvalid.append(i)
        elif texte == 'strFalse':
            strInvalid.append(i)
    
    if numberInvalid:
        return 'numberFalse',numberInvalid 
    elif strInvalid:
        return 'strFalse',strInvalid
    else:
        return all(s == "" for s in textes_recuperees),None

def create_new_drink(get_text):
    data_base_index = Db.choix_de_la_data_base
    index_boisson = Db.index_boisson
    textes_recuperees,names = get_text()
    
    print(names)
    for i in range(len(textes_recuperees)):
        texte = textes_recuperees[i]
        colonne = names[i]

        try :
            texte = float(texte)
        except :
            if "," in texte :
                texte  = texte.split(",")

        if colonne not in  ['PersonalRating', 'Comment', 'Favorite']:
            Db.dbsall[data_base_index][0].at[index_boisson,colonne] = texte
    print(Db.dbsall[data_base_index][0].iloc[index_boisson])
   

    add_uniques_element(get_text=get_text)

def add_uniques_element(get_text):
    textes_recuperees,names = get_text()
    data_base_index = Db.choix_de_la_data_base

    ## On rajoute toutes les nouvelles valeurs dans unique_element sans vérifier
    new_row = pd.Series() 
    Db.dbsall[data_base_index][1] = Db.dbsall[data_base_index][1]._append(new_row, ignore_index=True)
    new_index = len(Db.dbsall[data_base_index][1]) - 1      
    colomn_with_list_index = []

    for i in range(len(textes_recuperees)) :
        texte = textes_recuperees[i]
        if ',' in texte :
            colomn_with_list_index.append(i)
        else :
            colonne = names[i]
            Db.dbsall[Db.choix_de_la_data_base][1].at[new_index,colonne] = texte
    
    

    for index in colomn_with_list_index :
        texte_list = textes_recuperees[index]
        texte_list = texte_list.split(",")
        number_element = 1
        colonne = names[index]
        
        for texte in texte_list :

            Db.dbsall[Db.choix_de_la_data_base][1].at[new_index+number_element,colonne] = texte
            number_element +=1


    uniques_elements_columns_list = []

    for name in Db.dbsall[Db.choix_de_la_data_base][1].columns :
        uniques_elements_column = Db.dbsall[Db.choix_de_la_data_base][1][name].drop_duplicates()
        uniques_elements_columns_list.append(uniques_elements_column)

    new_unique_element = pd.DataFrame(dict(zip(Db.dbsall[Db.choix_de_la_data_base][1].columns,uniques_elements_columns_list)))



    Db.dbsall[Db.choix_de_la_data_base][1] = new_unique_element




