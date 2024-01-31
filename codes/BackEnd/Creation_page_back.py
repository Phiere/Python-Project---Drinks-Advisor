import pandas as pd
import Db_gestions as Db

def texte_vides(get_text):
    textes_recuperees,names = get_text()
    return all(s == "" for s in textes_recuperees)

def create_new_drink(data_base_index,get_text):
    textes_recuperees,names = get_text()
   
    new_row = pd.Series(textes_recuperees, index=names) #Attention c'est le Unamed 0 qui casse les couilles

    Db.dbsall[data_base_index][0] = Db.dbsall[data_base_index][0]._append(new_row, ignore_index=True)
    new_index = len(Db.dbsall[data_base_index][0]) - 1
    Db.index_boisson = new_index
    Db.dbsall[data_base_index][0].iloc[new_index,-1] = 0
    Db.dbsall[data_base_index][0].iloc[new_index,-3] = 0



        #newdf.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/codes/TrashFolder/test_creation.csv")



