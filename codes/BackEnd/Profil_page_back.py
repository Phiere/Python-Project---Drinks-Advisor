
import numpy
import pandas as pd
import Db_gestions as Db

categories = ['Vins', 'Cocktails', 'Cafés', 'Mocktails', 'Bières']
dbs = Db.dbsall

###1er élément (à droite): QVBox avec 2 graphiques
###1er graphique : Histogramme du nombre de boissons notées par catégorie
def nb_of_notes(df):
    if 'PersonalRating' in df.columns and not (len(df[df['PersonalRating'] != -1]) == 0):
        tempdf = df[df['PersonalRating'] != -1]
        return len(tempdf)
    else:
        return 0

def nb_notes_per_categories():
    nb_notes = []
    for i in range(len(Db.dbsall)):
        nb_notes.append(nb_of_notes(Db.dbsall[i][0]))
    return nb_notes

###2ème graphique : Histogramme des moyennes des notes par catégorie
def mean_of_note(df):
    if 'PersonalRating' in df.columns and not (len(df[df['PersonalRating'] != -1]) == 0):
        tempdf = df[df['PersonalRating'] != -1]
        return tempdf['PersonalRating'].mean()
    else:
        return 0  # Retourner une valeur spéciale pour indiquer l'absence de données

def mean_notes_per_categories():
    means_notes = []
    for i in range(len(Db.dbsall)):
        mean_note = mean_of_note(Db.dbsall[i][0])
        means_notes.append(float(mean_note))
    return means_notes


import pandas as pd

# Définir les noms des colonnes
noms_colonnes = ['Colonne1', 'Colonne2', 'Colonne3', 'Colonne4', 'Colonne5']

# Créer un DataFrame vide avec ces colonnes
df = pd.DataFrame(columns=noms_colonnes)



###2ème élément (à gauche): Liste des infos des boissons ajoutées aux Favoris
def favorites_extraction():
    column_names = ['Nom_db','Name','PersonalRating','Commentary','db','index']
    favories = pd.DataFrame(columns=column_names)

    for i in range(len(Db.dbsall)):
        data_frame = Db.dbsall[i][0]
        data_frame = data_frame[data_frame['Favories'] == 1]

        cut = data_frame[['Name', 'PersonalRating', 'Commentary']]
        cut['Nom_db'] = categories[i]
        cut['db'] = i
        cut['index'] = data_frame.index

        favories = pd.concat([favories, cut], axis=0)
 

    return favories