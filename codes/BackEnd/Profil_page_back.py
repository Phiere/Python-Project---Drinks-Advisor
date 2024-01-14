
import numpy
import Db_gestions as DB

categories = ['Vins', 'Cocktails', 'Cafés', 'Mocktails', 'Bières']
dbs = DB.initilisationSoft()[0]


###1er graphique : compte le nombre de boissons notées par catégorie
def nb_of_notes(df):
    tempdf = df['PersonalRating'].dropna()
    return len(tempdf)

def nb_notes_per_categories():
    nb_notes = [1,2,3,4,5]
    '''nb_notes.append(nb_of_notes(DB.Wines))
    nb_notes.append(nb_of_notes(DB.Cocktail))
    nb_notes.append(nb_of_notes(DB.Coffee))
    nb_notes.append(nb_of_notes(DB.Mocktail))
    nb_notes.append(nb_of_notes(DB.Beers))'''
    return nb_notes 



###2eme graphique : compte le nombre de favories notées par catégorie
def nb_of_favories(df):
    return len(df[df.Favoris == 1])


###4eme graphique : compte les moyennes des notes par catégorie
def mean_of_note(df):
    tempdf = df['PersonalRating'].dropna()
    return tempdf.mean()

def mean_notes_per_categories():
    means_notes = [1,2,3,4,5]
    '''means_notes.append(mean_of_note(DB.Wines))
    means_notes.append(mean_of_note(DB.Cocktail))
    means_notes.append(mean_of_note(DB.Coffee))
    means_notes.append(mean_of_note(DB.Mocktail))
    means_notes.append(mean_of_note(DB.Beers))
    for i in range(len(means_notes)):
        if pandas.isna(means_notes[i]) :
            means_notes[i] = 0'''
    return means_notes

dbs = DB.dbsall

def favoris_extraction():
    Exctration = []
    for i in range(len(dbs)):
        favorie = dbs[i][0]
        favorie = favorie [favorie['Favories'] == 1]
        favorie = favorie[['Name','PersonalRating','Commentary']]
        Exctration.append(favorie)
    return Exctration

def favories_count():
    favories_counting =[] 
    for i in range(len(dbs)):
        favorie = dbs[i][0]
        favorie = favorie [favorie['Favories'] == 1]
        favories_counting.append(len(favorie))
    return favories_counting

def notes_mean():
    note_means =[] 
    for i in range(len(dbs)):
        note_means.append(0)
        favorie = dbs[i][0]
        favorie = favorie [favorie['PersonalRating'] != -1]
        favorie = favorie [['PersonalRating']]
        favorie = favorie.astype(float)
        moyenne = favorie['PersonalRating'].mean()
        if not(numpy.isnan(moyenne)) :
            note_means[i] = moyenne
    return note_means
