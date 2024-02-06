import pandas as pd
import Db_gestions as Db

def texte_vides(get_text):
    textes_recuperees,names = get_text()
    return all(s == "" for s in textes_recuperees)

def create_new_drink(data_base_index,get_text):
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



        #newdf.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/codes/TrashFolder/test_creation.csv")



