
import numpy
import pandas as pd
import Db_gestions as DB

categories = ['Vins', 'Cocktails', 'Cafés', 'Mocktails', 'Bières']
dbs = DB.initilisationSoft()

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
    for i in range(len(DB.dbsall)):
        nb_notes.append(nb_of_notes(DB.dbsall[i][0]))
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
    for i in range(len(DB.dbsall)):
        mean_note = mean_of_note(DB.dbsall[i][0])
        means_notes.append(float(mean_note))
    return means_notes

dbs = DB.dbsall

###2ème élément (à gauche): Liste des infos des boissons ajoutées aux Favoris
def favorites_extraction():
    extraction = []
    for i in range(len(DB.dbsall)):
        favorite = DB.dbsall[i][0]
        favorite = favorite[favorite['Favories'] != 0]
        if (len(favorite)>0):
            favorite = favorite[['Name', 'PersonalRating', 'Commentary']]
            extraction.append(favorite)
        else:
            extraction.append(pd.DataFrame())
    return extraction