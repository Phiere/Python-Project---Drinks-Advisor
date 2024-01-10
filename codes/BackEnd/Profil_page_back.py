
import pandas
import Db_gestions as DB

categories = ['Vins', 'Cocktails', 'Cafés', 'Mocktails', 'Bières']



###1er graphique : compte le nombre de boissons notées par catégorie
def nb_of_notes(df):
    tempdf = df['PersonalRating'].dropna()
    return len(tempdf)

def nb_notes_per_categories():
    nb_notes = []
    nb_notes.append(nb_of_notes(DB.Wines))
    nb_notes.append(nb_of_notes(DB.Cocktail))
    nb_notes.append(nb_of_notes(DB.Coffee))
    nb_notes.append(nb_of_notes(DB.Mocktail))
    nb_notes.append(nb_of_notes(DB.Beers))
    return nb_notes 



###2eme graphique : compte le nombre de favories notées par catégorie
def nb_of_favories(df):
    return len(df[df.Favoris == 1])

def favories_per_categories():
    nb_favories = []
    nb_favories.append(nb_of_favories(DB.Wines))
    nb_favories.append(nb_of_favories(DB.Cocktail))
    nb_favories.append(nb_of_favories(DB.Coffee))
    nb_favories.append(nb_of_favories(DB.Mocktail))
    nb_favories.append(nb_of_favories(DB.Beers))
    return nb_favories 

###4eme graphique : compte les moyennes des notes par catégorie
def mean_of_note(df):
    tempdf = df['PersonalRating'].dropna()
    return tempdf.mean()

def mean_notes_per_categories():
    means_notes = []
    means_notes.append(mean_of_note(DB.Wines))
    means_notes.append(mean_of_note(DB.Cocktail))
    means_notes.append(mean_of_note(DB.Coffee))
    means_notes.append(mean_of_note(DB.Mocktail))
    means_notes.append(mean_of_note(DB.Beers))
    for i in range(len(means_notes)):
        if pandas.isna(means_notes[i]) :
            means_notes[i] = 0
    return means_notes



