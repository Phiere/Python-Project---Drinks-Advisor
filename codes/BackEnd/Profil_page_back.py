
import numpy
import pandas as pd
import Db_gestions as DB

categories = ['Vins', 'Cocktails', 'Cafés', 'Mocktails', 'Bières']
dbs = DB.initilisationSoft()[0]

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
def nb_of_favorites(df):
    if 'Favories' in df.columns and not (len(df[df['Favories'] != 0]) == 0):
        tempdf = df[df['Favories'] != 0]
        return len(tempdf)
    else:
        return 0

def favorites_extraction():
    extraction = []
    for i in range(len(DB.dbsall)):
        favorite = DB.dbsall[i][0]
        favorite = favorite[favorite['Favories'] != 0]
        if (len(favorite)>0):
            favorite = favorite[['Name', 'PersonalRating', 'Commentary']]
            extraction.append(favorite)
        else:
            extraction.append(0)
        #if favorite == [0, 0, 0, 0, 0]:
         #   extraction = 'Aucune boisson n''a été ajoutée aux Favoris'
    return extraction

def favorites_count():
    favorites_counting = []
    for i in range(len(DB.dbsall)):
        favorite = DB.dbsall[i][0]
        favorite = favorite[favorite['Favories'] > 0]
        if (len(favorite)>0):
            favorites_counting.append(len(favorite))
        else:
            favorites_counting.append(0)
    return favorites_counting

""" Inutile au final
def notes_mean():
    note_means = [] 
    for i in range(len(dbs)):
        note_means.append(0)
        favorie = dbs[i][0]
        favorie = favorie [favorie['PersonalRating'] != -1]
        favorie = favorie [['PersonalRating']]
        favorie = favorie.astype(float)
        moyenne = favorie['PersonalRating'].mean()
        if not(numpy.isnan(moyenne)) :
            note_means[i] = moyenne
    return note_means"""
