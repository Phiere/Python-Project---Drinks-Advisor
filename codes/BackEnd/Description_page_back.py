##############################
#Ce script contient les fonctions de back_end pour la création de l'écran description. Toutes
#les fonctions crées ici seront utilisées dans le script : Description_page_UI.
##############################

import Db_gestions as Db
import pandas as pd
import random


def get_name_from_drink():
    """Récupère le nom principal de la boisson"""
    db,index = Db.choix_de_la_data_base,Db.index_boisson
    try :
        boisson = Db.dbsall[db][0].iloc[index]
    except IndexError:
        IndexError("single positional indexer is out-of-bounds")
        name = "Unfilled(errorindex)"
    else:
        name = boisson['Name']
    finally:
        return name 

try:
    # Code à tester
    resultat = 10 / 0
except ZeroDivisionError:
    # Code pour gérer l'erreur spécifique
    print("Erreur : Division par zéro.")
else:
    # Code à exécuter si le bloc try ne lève pas d'exception
    print("La division a réussi !")
finally:
    # Code de nettoyage, exécuté qu'il y ait eu une erreur ou non
    print("Opération de division terminée.")



def get_description_from_drink():
    """Récupère les éléments de description de la boisson en les mettant en forme correctement"""
    db,index = Db.choix_de_la_data_base,Db.index_boisson
    boisson = Db.dbsall[db][0].iloc[index]
    columns_to_read = Db.dbsall[db][3]
    text = ""
    skip_next_iterations = False

    for colonne in columns_to_read :
        if skip_next_iterations:
            break 

        value = boisson[colonne]

        if isinstance(value, list):
            value_str = ', '.join(str(item) for item in value)
        elif colonne == 'Price' and str(value) != 'Unfilled':
            if Db.choix_de_la_data_base == 0 : 
                value_str = f"{value} $"
            elif Db.choix_de_la_data_base == 3: 
                value_str = f"{value} $/100g"
        elif colonne == 'ReviewsNumber':
            value_str = f"{int(boisson[colonne]):,}"
        elif value not in ['',' ', 'nan']:
            value_str = str(value)

        if value_str.startswith('[') and value_str.endswith(']'):
            value_list = [item.strip("' ") for item in value_str[1:-1].split(',')]
            seen_elements = set()
            value_list_filtered = [item for item in value_list if item != 'Unfilled' and item != '' and item != "-1.0"  and item != ' ' and (item not in seen_elements and seen_elements.add(item) is None)]
            value_str = ', '.join(value_list_filtered)
        
        text += str(colonne) + ' : ' + value_str + '\n' + '\n'

        if Db.choix_de_la_data_base == 2 and colonne == 'ReviewsNumber':
            text += "Rating (/5) : \n"
            index_OverallReview = columns_to_read.index('ReviewsNumber')
            for colonne in columns_to_read[index_OverallReview+1:]:
                text += '\n' + f"   - {str(colonne)} : {int(boisson[colonne]):,}" + '\n'
            skip_next_iterations = True            
    return text


def get_status_favori():
    """Récupère le statut de favori de la boisson"""
    db,index =  Db.choix_de_la_data_base,Db.index_boisson
    favory = Db.dbsall[db][0].at[index,'Favorite']
    print('favory',favory)
    if  isinstance(favory,str):
        return favory == "1" or favory == "1.0"
    if isinstance(favory,bool) :
        return favory == True
    else :
        return favory == 1.0 or favory == 1


def update_status_favori():
    """Met à jour le statut de favori la boisson"""
    db,index =  Db.choix_de_la_data_base, Db.index_boisson
    favory = (Db.dbsall[db][0].iloc[index][-1])
    Db.dbsall[db][0].at[index,'Favorite'] = not(favory)
    return favory


def get_comment():
    """Récupère le commentaire associée à la boisson"""
    db,index =  Db.choix_de_la_data_base, Db.index_boisson
    comment = Db.dbsall[db][0].at[index,'Comment']
    if pd.isna(comment): return 'Unfilled'
    return comment


def update_comment(commentary):
    """Met à jour le commentaire de la boisson choisie
    
    - commentary : texte à mettre en commentaire"""
    db,index =  Db.choix_de_la_data_base, Db.index_boisson
    Db.dbsall[db][0].at[index,'Comment'] = commentary


def get_rating():
    """Récupère la note de la boisson choisie
    
    - rating : note de la boisson choisie (int)"""
    db,index = Db.choix_de_la_data_base,  Db.index_boisson
    rating = Db.dbsall[db][0].at[index,'PersonalRating']
    return rating


def update_rating(rating):
    """Met à jour la note de la boisson choisie
    
    - rating : nouvelle note de la boison (int)"""
    db,index =  Db.choix_de_la_data_base,Db.index_boisson
    Db.dbsall[db][0].at[index,'PersonalRating'] = rating

########
##Tests 
########  
    
def test_get_name_from_drink(nb_test):
    """Fonction de test sur get_name_from_drink"""
    print("test_get_name_from_drink")
    for i in range(nb_test):
        index_db_rand = random.randint(0,4)
        db= Db.dbsall[index_db_rand][0]
        index_drink_rand = random.randint(0,len(db)-1)
        Db.choix_de_la_data_base = index_db_rand
        Db.index_boisson = index_drink_rand
        print(f"Test {i}")
        print("db, ligne ",index_db_rand,index_drink_rand)
        print("retour fonction ",get_name_from_drink())
    print("\n")
    
def test_get_description_from_drink(nb_test):
    """Fonction de test sur get_description_from_drink"""
    print("test_get_description_from_drink")
    for i in range(nb_test):
        index_db_rand = random.randint(0,4)
        db= Db.dbsall[index_db_rand][0]
        index_drink_rand = random.randint(0,len(db)-1)
        Db.choix_de_la_data_base = index_db_rand
        Db.index_boisson = index_drink_rand
        print(f"Test {i}")
        print("db, ligne ",index_db_rand,index_drink_rand)
        print("retour fonction ",get_description_from_drink())
    print("\n")

def test_get_status_favory(nb_test):
    """Fonction de test sur get_status_favori"""
    print("test_get_status_favory")
    for i in range(nb_test):
        index_db_rand = random.randint(0,4)
        db= Db.dbsall[index_db_rand][0]
        index_drink_rand = random.randint(0,len(db)-1)
        Db.choix_de_la_data_base = index_db_rand
        Db.index_boisson = index_drink_rand
        print(f"Test {i}")
        print("db, ligne ",index_db_rand,index_drink_rand)
        print("retour fonction ",get_status_favori())
    print("\n")

def test_update_status_favori(nb_test):
    """Fonction de test sur update_status_favori"""
    print("test_get_status_favory")
    for i in range(nb_test):
        index_db_rand = random.randint(0,4)
        db= Db.dbsall[index_db_rand][0]
        index_drink_rand = random.randint(0,len(db)-1)
        Db.choix_de_la_data_base = index_db_rand
        Db.index_boisson = index_drink_rand
        print(f"Test {i}")
        print("db, ligne ",index_db_rand,index_drink_rand)
        print("retour fonction avant update",get_status_favori())
        update_status_favori()
        print("retour fonction après update",get_status_favori())
    print("\n")
    
def test_get_comment(nb_test):
    """Fonction de test sur get_comment"""
    print('test_get_comment')
    for i in range(nb_test):
        index_db_rand = random.randint(0,4)
        db= Db.dbsall[index_db_rand][0]
        index_drink_rand = random.randint(0,len(db)-1)
        Db.choix_de_la_data_base = index_db_rand
        Db.index_boisson = index_drink_rand
        print(f"Test {i}")
        print("db, ligne ",index_db_rand,index_drink_rand)
        print("retour fonction ",get_comment())
    print("\n")

def test_update_comment(nb_test):
    """Fonction de test sur get_rating"""
    for i in range(nb_test):
        index_db_rand = random.randint(0,4)
        db= Db.dbsall[index_db_rand][0]
        index_drink_rand = random.randint(0,len(db)-1)
        Db.choix_de_la_data_base = index_db_rand
        Db.index_boisson = index_drink_rand
        print(f"Test {i}")
        print("db, ligne ",index_db_rand,index_drink_rand)
        print("retour fonction avant update",get_comment())
        comment = random.choice(["","Commentaire","    ","JFZOJ"])
        print("update : ", comment)
        update_comment(commentary=comment)
        print("retour fonction après update",get_comment())
    print("\n")
    
def test_get_rating(nb_test):
    """Fonction de test sur get_rating"""
    print("test_get_rating")
    for i in range(nb_test):
        index_db_rand = random.randint(0,4)
        db= Db.dbsall[index_db_rand][0]
        index_drink_rand = random.randint(0,len(db)-1)
        Db.choix_de_la_data_base = index_db_rand
        Db.index_boisson = index_drink_rand
        print(f"Test {i}")
        print("db, ligne ",index_db_rand,index_drink_rand)
        print("retour fonction ",get_rating())
    print("\n")

def test_update_rating(nb_test):
    """Fonction de test sur update_rating"""
    print("test_update_rating")
    for i in range(nb_test):
        index_db_rand = random.randint(0,4)
        db= Db.dbsall[index_db_rand][0]
        index_drink_rand = random.randint(0,len(db)-1)
        Db.choix_de_la_data_base = index_db_rand
        Db.index_boisson = index_drink_rand
        print(f"Test {i}")
        print("db, ligne ",index_db_rand,index_drink_rand)
        print("retour fonction avant update",get_rating())
        rating = random.randint(0,5)
        print("update : ",rating)
        update_rating(rating=rating)
        print("retour fonction après update",get_rating())
    print("\n")

if __name__ == '__main__':
    test = input("Tester les fonctions du script ? (0/1) : ")
    if test : 
        nb_test = 1
        test_get_description_from_drink(nb_test)
        test_get_description_from_drink(nb_test)
        test_get_status_favory(nb_test)
        test_update_status_favori(nb_test)
        test_get_comment(nb_test)
        test_update_comment(nb_test)
        test_get_rating(nb_test)
        test_update_rating(nb_test)
    