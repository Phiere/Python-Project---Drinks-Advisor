import pandas as pd
import Db_gestions as Db

#V0.1
def nb_of_notes(df):
    """Donne le nombre de boisson notée dans un data_frame
    
    - Data_frame dont on veut le nombre de boisson notées (data_frame)
    - return : int(nombre de boisson notées)"""
    if 'PersonalRating' in df.columns and not (len(df[df['PersonalRating'] != -1]) == 0):
        tempdf = df[df['PersonalRating'] > 0]
        return len(tempdf)
    else:
        return 0

#V0.1
def nb_notes_per_categories():
    """Donne le nombre de boissons notées par data_base"""
    nb_notes = []
    for i in range(len(Db.dbsall)):
        nb_notes.append(nb_of_notes(Db.dbsall[i][0]))
    return nb_notes

#V0.1
def mean_of_note(df):
    """Donne la moyenne des notes des boissons notées dans un data_frame
    
    - Data_frame dont on veut la moyenne des notes des boissons notées (data_frame)
    - return : int(moyenne des boissons notéess)"""
    if 'PersonalRating' in df.columns and not (len(df[df['PersonalRating'] != -1]) == 0):
        tempdf = df[df['PersonalRating'] > 0]
        return tempdf['PersonalRating'].mean()
    else:
        return 0  # Retourner une valeur spéciale pour indiquer l'absence de données

#V0.1
def mean_notes_per_categories():
    """Donne la moyenne des notes par data_base"""
    means_notes = []
    for i in range(len(Db.dbsall)):
        mean_note = mean_of_note(Db.dbsall[i][0])
        means_notes.append(float(mean_note))
    return means_notes

#V0.1
def favorites_extraction():
    """Donne la liste des éléments mis en favories dans chaque data_base
    
    -return : data_frame des boissons mis en favori"""
    column_names = ['Nom_db','Name','PersonalRating','Comment','db','index']
    favories = pd.DataFrame(columns=column_names)

    for i in range(len(Db.dbsall)):
        data_frame = Db.dbsall[i][0]
        data_frame = data_frame[data_frame['Favorite'] == 1]

        cut = data_frame[['Name', 'PersonalRating']]
        cut['Nom_db'] = Db.categories[i]
        cut['db'] = i
        cut['index'] = data_frame.index

        favories = pd.concat([favories, cut], axis=0)

    return favories

#V0.1
#Pas fan d'appeler les indices au lieu des noms mais sinon ça fonctionne pas :()
def get_favorites_informations(favories_dfs,index):
    """Retourne les informations d'affichage sur la boisson mise en favoris."""
    texte = [str(favories_dfs.iat[index,j]) for j in range(len(['Nom_db','Name','PersonalRating']))]                
    index_db = favories_dfs.iat[index,-2]
    index_boisson = favories_dfs.iat[index,-1]
    return texte,index_db,index_boisson

##Tests