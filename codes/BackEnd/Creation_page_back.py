import pandas as pd
import Db_gestions as Db


dbs = Db.initilisationSoft()[0]

def create_new_drink(data_base_index,get_text):

    data_base = Db.dbsall[data_base_index][0]
    textes_recuperees = get_text()

    new_row = pd.Series(textes_recuperees, index=data_base.columns[1:]) #Attention c'est le Unamed 0 qui casse les couilles

    Db.dbsall[data_base_index][0] = Db.dbsall[data_base_index][0]._append(new_row, ignore_index=True)

    #newdf.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/codes/TrashFolder/test_creation.csv")



