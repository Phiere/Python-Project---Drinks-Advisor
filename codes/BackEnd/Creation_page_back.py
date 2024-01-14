import pandas as pd
import Db_gestions as Db


dbs = Db.initilisationSoft()[0]

def create_new_drink(data_frame,liste_colonnes):
    textes_recuperees = liste_colonnes.get_texts()
    newdf = data_frame.copy()

    new_row = pd.Series(textes_recuperees, index=newdf.columns)

    newdf= newdf._append(new_row, ignore_index=True)
    newdf.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/codes/TrashFolder/test_creation.csv")
    print(textes_recuperees)


