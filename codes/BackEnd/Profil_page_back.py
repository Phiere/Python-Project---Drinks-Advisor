import pandas as pd
import Db_gestions as Db


def nb_of_notes(df):
    """Donne le nombre de boissons notées dans un data_frame
    
    - df : Data_frame dont on veut le nombre de boisson notées (data_frame)
    - return : int(nombre de boissons notées)"""
    if 'PersonalRating' in df.columns and not (len(df[df['PersonalRating'] != -1]) == 0):
        tempdf = df[df['PersonalRating'] > 0]
        return len(tempdf)
    else:
        return 0


def nb_notes_per_categories():
    """Donne le nombre de boissons notées par data_base"""
    nb_notes = []
    for i in range(len(Db.dbsall)):
        nb_notes.append(nb_of_notes(Db.dbsall[i][0]))
    return nb_notes


def mean_of_note(df):
    """Donne la moyenne des notes des boissons notées dans un data_frame
    
    - df : Data_frame dont on veut la moyenne des notes des boissons notées (data_frame)
    - return : int(moyenne des boissons notées)"""
    if 'PersonalRating' in df.columns and not (len(df[df['PersonalRating'] != -1]) == 0):
        tempdf = df[df['PersonalRating'] > 0]
        return tempdf['PersonalRating'].mean()
    else:
        return 0  # Retourner une valeur spéciale pour indiquer l'absence de données


def mean_notes_per_categories():
    """Donne la moyenne des notes par data_base"""
    means_notes = []
    for i in range(len(Db.dbsall)):
        mean_note = mean_of_note(Db.dbsall[i][0])
        means_notes.append(float(mean_note))
    return means_notes

#??
def favorites_extraction():
    """Donne la liste des éléments mis en favori dans chaque data_base
    
    -return : data_frame des boissons mises en favori"""
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

#??
def get_favorites_informations(favories_dfs,index):
    """Retourne les informations d'affichage sur la boisson mise en favori."""
    texte = [str(favories_dfs.iat[index,j]) for j in range(3)]                
    index_db = favories_dfs.iat[index,-2]
    index_boisson = favories_dfs.iat[index,-1]
    return texte,index_db,index_boisson

########
##Tests
########

def test_nb_notes():
    """Fonction de test pour la fonction nb_notes"""
    print("test_nb_notes")
    #Test0
    db = Db.dbsall[0][0]
    nb_votes_df0 = 5
    print("Test 0 : ", nb_votes_df0 == nb_of_notes(db))

    #Test1
    db = Db.dbsall[1][0]
    nb_votes_df1 = 4
    print("Test 1 : ", nb_votes_df1 == nb_of_notes(db))

    #Test2
    db = Db.dbsall[2][0]
    nb_votes_df2 = 0
    print("Test 2 : ", nb_votes_df2 == nb_of_notes(db))

    #Test3
    db = Db.dbsall[3][0]
    nb_votes_df3 = 1
    print("Test 3 : ", nb_votes_df3 == nb_of_notes(db))

    #Test4
    db = Db.dbsall[4][0]
    nb_votes_df4 = 10
    print("Test 4 : ", nb_votes_df4 == nb_of_notes(db))

def test_nb_notes_per_categories():
    """Fonction de test pour la fonction nb_notes_per_categories"""
    print("test_nb_notes_per_categories")
    #Test0
    nb_votes_percategorie_df0 = [5,4,0,1,10]
    print("Test 0 : ", nb_votes_percategorie_df0 == nb_notes_per_categories())

def test_mean_of_note():
    """Fonction de test pour la fonction mean_of_note"""
    print("test_nb_notes")
    #Test0
    db = Db.dbsall[0][0]
    mean_of_note0 = 3.0
    print("Test 0 : ", mean_of_note0 == mean_of_note(db))

    #Test1
    db = Db.dbsall[1][0]
    mean_of_note0 = 3.5
    print("Test 1 : ", mean_of_note0 == mean_of_note(db))

    #Test2
    db = Db.dbsall[2][0]
    mean_of_note2 = 0.0
    print("Test 2 : ", mean_of_note2 == mean_of_note(db))

    #Test3
    db = Db.dbsall[3][0]
    mean_of_note3 = 5.0
    print("Test 3 : ", mean_of_note3 == mean_of_note(db))

    #Test4
    db = Db.dbsall[4][0]
    mean_of_note4 = 2.7
    print("Test 4 : ", mean_of_note4 == mean_of_note(db))

def test_mean_notes_per_categories():
    """Fonction de test pour la fonction nb_notes"""
    print("test_mean_notes_per_categories")
    #Test0
    mean_notes_per_categories0 = [3.0,3.5,0.0,5.0,2.7]
    print("Test 0 : ", mean_notes_per_categories0 == mean_notes_per_categories())

def test_favorite_exctaction():
    pass

def test_get_favorites_informations():
    pass

if __name__ == '__main__':
    test = input("Tester les fonctions du script ? (0/1) : ")
    if test : 
        test_nb_notes()
        test_nb_notes_per_categories()
        test_mean_of_note()
        test_mean_notes_per_categories()
        test_favorite_exctaction()
        test_favorite_exctaction()
        test_get_favorites_informations()
