##############################
#Ce script contient les fonctions de back_end pour la création de l'écran profil. Toutes
#les fonctions crées ici seront utilisées dans le script : Profil_page_UI.
##############################

import pandas as pd
import Db_gestions as Db
import random


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
    favories = favories.sort_values(by = 'PersonalRating',ascending=False)
    return favories


def get_favorites_informations(favories_dfs,index):
    """Retourne les informations d'affichage sur la boisson mise en favori."""
    texte = [str(favories_dfs.iat[index,j]) for j in range(3)]                
    index_db = favories_dfs.iat[index,-2]
    index_boisson = favories_dfs.iat[index,-1]
    return texte,index_db,index_boisson

########
##Tests
########

def test_nb_notes(nb_test):
    """Fonction de test pour la fonction nb_notes"""
    print("test_nb_notes")
    for i in range(nb_test):
        print(f"Test {i}")
        index_db_rand = random.randint(0,4)
        db= Db.dbsall[index_db_rand][0]
        Db.choix_de_la_data_base = index_db_rand
        notes_de_base = nb_of_notes(db)
        nb_modif = random.randint(0,10)
        for index in random.sample(range(0,len(db)-1),10):
            nb_modif +=1
            Db.dbsall[index_db_rand][0].at[index,'PersonalRating'] = random.randint(1,5)
        print("nombre de votes ajoutés : ",nb_modif)
        print("retour fonction ",nb_of_notes(Db.dbsall[index_db_rand][0])-notes_de_base)
    print("\n")

def test_nb_notes_per_categories(nb_test):
    """Fonction de test pour la fonction nb_notes_per_categories"""
    print("test_nb_notes_per_categories")
    for i in range(nb_test):
        print(f"Test {i}")
        notes_de_bases = []
        notes_ajoute = []
        for k in range(5) :
            Db.choix_de_la_data_base = k
            db= Db.dbsall[k][0]
            
            notes_de_base = nb_of_notes(db)
            nb_modif = random.randint(0,50)
            for index in random.sample(range(0,len(db)-1),10):
                nb_modif +=1
                Db.dbsall[k][0].at[index,'PersonalRating'] = random.randint(1,5)
            notes_de_bases.append(notes_de_base)
            notes_ajoute.append(nb_modif)
     
        print("nombre de votes ajoutés : ",notes_ajoute)
        print(notes_de_bases)
        print("retour fonction ",[a-b for a,b in zip(nb_notes_per_categories(),notes_de_bases)])
    print("\n")

def test_mean_of_note(nb_test):
    """Fonction de test pour la fonction mean_of_note"""
    print("test_nb_notes")
    for i in range(nb_test):
        print(f"Test {i}")
        index_db_rand = random.randint(0,4)
        db= Db.dbsall[index_db_rand][0]
        Db.choix_de_la_data_base = index_db_rand
        mean_base = mean_of_note(db)*nb_of_notes(db)
        nb_modif = random.randint(0,50)
        new_mean = 0
        for index in random.sample(range(0,len(db)-1),10):
            nb_modif +=1
            new_note = random.randint(1,5)
            Db.dbsall[index_db_rand][0].at[index,'PersonalRating'] = new_note
            new_mean += new_note
        new_mean = new_mean
        print("Moyennes ajoutée : ",new_mean/nb_modif)
        print("retour fonction ",(mean_of_note(db)*nb_of_notes(db) - mean_base)/nb_modif)
    print("\n")

def test_mean_notes_per_categories(nb_test):
    """Fonction de test pour la fonction nb_notes"""
    print("test_mean_notes_per_categories")
    for i in range(nb_test):
        print(f"Test {i}")
        mean_base = []
        nb_modifs = []
        mean_added = []
        for k in range(4):
            Db.choix_de_la_data_base = k
            db= Db.dbsall[k][0]
            mean_base.append(mean_of_note(db)*nb_of_notes(db))
            nb_modif = random.randint(0,50)
            nb_modifs = 0
            new_mean = 0
            for index in random.sample(range(0,len(db)-1),10):
                nb_modif +=1
                new_note = random.randint(0,5)
                Db.dbsall[k][0].at[index,'PersonalRating'] = new_note
                new_mean += new_note
            mean_added.append(new_mean/nb_modif)

        print("Moyennes ajoutée : ",mean_added)
        print("retour fonction ",[(a*b-c)/d for a,b,c,d in zip(mean_notes_per_categories(),nb_notes_per_categories(),mean_base,nb_modifs)])
    print("\n")

def test_favorite_exctaction(nb_test):
    print("test_favorite_exctaction")
    for i in range(nb_test):
        index_db_rand = random.randint(0,4)
        db= Db.dbsall[index_db_rand][0]
        index_drink_rand = random.randint(0,len(db)-1)
        Db.choix_de_la_data_base = index_db_rand
        Db.index_boisson = index_drink_rand
        print(f"Test {i}")
        print("db, ligne ",index_db_rand,index_drink_rand)
        print("favori déjà présents :", favorites_extraction())
        changements = []
        for k in range(random.randint(0,10)):
            p = random.randint(0,len(db)-1)
            changements.append(p)
            Db.dbsall[index_db_rand][0].loc[index_drink_rand,'Favorite'] = not(Db.dbsall[index_db_rand][0].loc[index_drink_rand,'Favorite'])
        print("changements aux index :", changements)
        print("retour fonction ",favorites_extraction())
    print("\n")

def test_get_favorites_informations(nb_test):
    """Test de la fonction get_favorites_informations"""
    print("Test get favorite exctraction")
    favoris = favorites_extraction()
    print("favoris :", favoris)
    taille = len(favoris)-1
    if taille < nb_test : return "Trop de test"
    print("retour fonction :")
    for i in random.sample(range(0,taille),nb_test):
        print(get_favorites_informations(favoris,i))
    print("\n")

    
if __name__ == '__main__':
    test = input("Tester les fonctions du script ? "+"\n"+"Attention les tests doivent être faits sur des bases de données non modifies (0/1) : ")
    if test : 
        nb_test = 3
        test_nb_notes(nb_test)
        test_nb_notes_per_categories(nb_test)
        test_mean_of_note(nb_test)
        test_mean_notes_per_categories(nb_test)
        test_favorite_exctaction(nb_test)
        test_get_favorites_informations()
