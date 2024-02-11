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

def test_nb_notes():
    """Fonction de test pour la fonction nb_notes"""
    print("test_nb_notes")
    #Test0
    Db.choix_de_la_data_base = 0
    nb_votes_df0 = 0
    print("Test 0 : ", nb_votes_df0 == nb_of_notes())

    #Test1
    Db.choix_de_la_data_base = 0
    nb_votes_df1 = 0
    print("Test 1 : ", nb_votes_df1 == nb_of_notes())

    #Test2
    Db.choix_de_la_data_base = 0
    nb_votes_df2 = 0
    print("Test 2 : ", nb_votes_df2 == nb_of_notes())

    #Test3
    Db.choix_de_la_data_base = 0
    nb_votes_df3 = 0
    print("Test 3 : ", nb_votes_df3 == nb_of_notes())

    #Test4
    Db.choix_de_la_data_base = 0
    nb_votes_df4 = 0
    print("Test 4 : ", nb_votes_df4 == nb_of_notes())

    #Test5
    Db.choix_de_la_data_base = 0
    nb_votes_df5 = 0
    print("Test 5 : ", nb_votes_df5 == nb_of_notes())

def test_nb_notes_per_categories():
    """Fonction de test pour la fonction nb_notes_per_categories"""
    print("test_nb_notes_per_categories")
    #Test0
    nb_votes_percategorie_df0 = [0,0,0,0,0]
    print("Test 0 : ", nb_votes_percategorie_df0 == nb_notes_per_categories())

    #Test1
    nb_votes_percategorie_df1 = [0,0,0,0,0]
    print("Test 1 : ", nb_votes_percategorie_df1 == nb_notes_per_categories())

    #Test2
    nb_votes_percategorie_df2 = [0,0,0,0,0]
    print("Test 2 : ", nb_votes_percategorie_df2 == nb_notes_per_categories())

    #Test3
    nb_votes_percategorie_df3 = [0,0,0,0,0]
    print("Test 3 : ", nb_votes_percategorie_df3 == nb_notes_per_categories())

    #Test4
    nb_votes_percategorie_df4 = [0,0,0,0,0]
    print("Test 4 : ", nb_votes_percategorie_df4 == nb_notes_per_categories())

def test_mean_of_note():
    """Fonction de test pour la fonction mean_of_note"""
    print("test_nb_notes")
    #Test0
    Db.choix_de_la_data_base = 0
    mean_of_note0 = 0
    print("Test 0 : ", mean_of_note0 == mean_of_note())

    #Test1
    Db.choix_de_la_data_base = 0
    mean_of_note0 = 0
    print("Test 1 : ", mean_of_note0 == mean_of_note())

    #Test2
    Db.choix_de_la_data_base = 0
    mean_of_note2 = 0
    print("Test 2 : ", mean_of_note2 == mean_of_note())

    #Test3
    Db.choix_de_la_data_base = 0
    mean_of_note3 = 0
    print("Test 3 : ", mean_of_note3 == mean_of_note())

    #Test4
    Db.choix_de_la_data_base = 0
    mean_of_note4 = 0
    print("Test 4 : ", mean_of_note4 == mean_of_note())

    #Test5
    Db.choix_de_la_data_base = 0
    mean_of_note5 = 0
    print("Test 5 : ", mean_of_note5 == mean_of_note())

def test_mean_notes_per_categories():
    """Fonction de test pour la fonction nb_notes"""
    print("test_mean_notes_per_categories")
    #Test0
    mean_notes_per_categories0 = [0,0,0,0,0]
    print("Test 0 : ", mean_notes_per_categories0 == mean_notes_per_categories())

    #Test1
    mean_notes_per_categories1 = [0,0,0,0,0]
    print("Test 1 : ", mean_notes_per_categories1 == mean_notes_per_categories())

    #Test2
    mean_notes_per_categories2 = [0,0,0,0,0]
    print("Test 2 : ", mean_notes_per_categories2 == mean_notes_per_categories())

    #Test3
    mean_notes_per_categories3 = [0,0,0,0,0]
    print("Test 3 : ", mean_notes_per_categories3 == mean_notes_per_categories())

    #Test4
    mean_notes_per_categories4 = [0,0,0,0,0]
    print("Test 4 : ", mean_notes_per_categories4 == mean_notes_per_categories())

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
