import Db_gestions as Db
import pandas as pd

#V0.2
def get_name_from_drink():
    """Récupère le nom principal de la boisson"""
    db,index = Db.choix_de_la_data_base,Db.index_boisson
    boisson = Db.dbsall[db][0].iloc[index]
    name = boisson['Name']
    return name 

#V0.0
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

#V0.2  
def get_status_favori():
    """Récupère le statut de favori de la boisson"""
    db,index =  Db.choix_de_la_data_base,Db.index_boisson
    favory = Db.dbsall[db][0].at[index,'Favorite']
    return favory

#V0.2
def update_status_favori():
    """Met à jour le statut de favori la boisson"""
    db,index =  Db.choix_de_la_data_base, Db.index_boisson
    favory = not(Db.dbsall[db][0].iloc[index][-1])
    Db.dbsall[db][0].at[index,'Favorite'] = favory
    return favory

#V0.2
def get_comment():
    """Récupère le commentaire associée à la boisson"""
    db,index =  Db.choix_de_la_data_base, Db.index_boisson
    comment = Db.dbsall[db][0].at[index,'Comment']
    if pd.isna(comment): return 'Leave a comment on the drink...'
    return comment

#V0.2
def update_comment(commentary):
    """Met à jour le commentaire de la boisson choisie
    
    - commentary : texte à mettre en commentaire"""
    db,index =  Db.choix_de_la_data_base, Db.index_boisson
    Db.dbsall[db][0].at[index,'Comment'] = commentary

#V0.2
def get_rating():
    """Récupère la note de la boisson choisie
    
    - rating : note de la boisson choisie (int)"""
    db,index = Db.choix_de_la_data_base,  Db.index_boisson
    rating = Db.dbsall[db][0].at[index,'PersonalRating']
    return rating

#V0.2
def update_rating(rating):
    """Met à jour la note de la boisson choisie
    
    - rating : nouvelle note de la boison (int)"""
    db,index =  Db.choix_de_la_data_base,Db.index_boisson
    Db.dbsall[db][0].at[index,'PersonalRating'] = rating

##Tests   
    
def test_get_name_from_drink():
    """Fonction de test sur get_name_from_drink"""
    print("test_get_name_from_drink")
    #Test 0
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name0 = 0
    print('Test 0 : ',get_name_from_drink() ==name0)

    #Test 1
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name1 = 0
    print('Test 1 : ',get_name_from_drink() ==name1)

    #Test 2
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name2 = 0
    print('Test 2 : ',get_name_from_drink() ==name2)

    #Test 3
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name3 = 0
    print('Test 3 : ',get_name_from_drink() ==name3)

    #Test 4
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name4 = 0
    print('Test 4 : ',get_name_from_drink() ==name4)

    #Test 5
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name5 = 0
    print('Test 5 : ',get_name_from_drink() ==name5)

def test_get_description_from_drink():
    """Fonction de test sur get_description_from_drink"""
    print("test_get_description_from_drink")
    #Test 0
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name0 = 0
    print('Test 0 : ',get_description_from_drink() ==name0)

    #Test 1
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name1 = 0
    print('Test 1 : ',get_description_from_drink() ==name1)

    #Test 2
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name2 = 0
    print('Test 2 : ',get_description_from_drink() ==name2)

    #Test 3
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name3 = 0
    print('Test 3 : ',get_description_from_drink() ==name3)

    #Test 4
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name4 = 0
    print('Test 4 : ',get_description_from_drink() ==name4)

    #Test 5
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name5 = 0
    print('Test 5 : ',get_description_from_drink() ==name5)

def test_get_status_favory():
    """Fonction de test sur get_status_favori"""
    print("test_get_status_favory")
    #Test 0
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name0 = 0
    print('Test 0 : ',get_status_favori() ==name0)

    #Test 1
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name1 = 0
    print('Test 1 : ',get_status_favori() ==name1)

    #Test 2
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name2 = 0
    print('Test 2 : ',get_status_favori() ==name2)

    #Test 3
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name3 = 0
    print('Test 3 : ',get_status_favori() ==name3)

    #Test 4
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name4 = 0
    print('Test 4 : ',get_status_favori() ==name4)

    #Test 5
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name5 = 0
    print('Test 5 : ',get_status_favori() ==name5)

def test_update_status_favori():
    """Fonction de test sur update_status_favori"""
    
    print("test_update_status_favori")
    #Test 0
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name0 = 0
    update_status_favori(name0)
    print('Test 0 : ',get_status_favori() ==name0)

    #Test 1
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name1 = 0
    update_status_favori(name1)
    print('Test 1 : ',get_status_favori() ==name1)

    #Test 2
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name2 = 0
    update_status_favori(name2)
    print('Test 2 : ',get_status_favori() ==name2)

    #Test 3
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name3 = 0
    update_status_favori(name3)
    print('Test 3 : ',get_status_favori() ==name3)

    #Test 4
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name4 = 0
    update_status_favori(name4)
    print('Test 4 : ',get_status_favori() ==name4)

    #Test 5
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name5 = 0
    update_status_favori(name5)
    print('Test 5 : ',get_status_favori() ==name5)

def test_get_comment():
    """Fonction de test sur get_comment"""
    print('test_get_comment')
    #Test 0
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name0 = 0
    print('Test 0 : ',get_comment() ==name0)

    #Test 1
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name1 = 0
    print('Test 1 : ',get_comment() ==name1)

    #Test 2
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name2 = 0
    print('Test 2 : ',get_comment() ==name2)

    #Test 3
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name3 = 0
    print('Test 3 : ',get_comment() ==name3)

    #Test 4
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name4 = 0
    print('Test 4 : ',get_comment() ==name4)

    #Test 5
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name5 = 0
    print('Test 5 : ',get_comment() ==name5)

def test_update_comment():
    """Fonction de test sur get_rating"""
    print("test_update_comment")
    #Test 0
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name0 = 0
    update_comment(name0)
    print('Test 0 : ',get_comment() ==name0)

    #Test 1
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name1 = 0
    update_comment(name1)
    print('Test 1 : ',get_comment() ==name1)

    #Test 2
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name2 = 0
    update_comment(name2)
    print('Test 2 : ',get_comment() ==name2)

    #Test 3
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name3 = 0
    update_comment(name3)
    print('Test 3 : ',get_comment() ==name3)

    #Test 4
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name4 = 0
    update_comment(name4)
    print('Test 4 : ',get_comment() ==name4)

    #Test 5
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name5 = 0
    update_comment(name5)
    print('Test 5 : ',get_comment() ==name5)

def test_get_rating():
    """Fonction de test sur get_rating"""
    print("test_get_rating")
    #Test 0
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name0 = 0
    print('Test 0 : ',get_rating() ==name0)

    #Test 1
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name1 = 0
    print('Test 1 : ',get_rating() ==name1)

    #Test 2
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name2 = 0
    print('Test 2 : ',get_rating() ==name2)

    #Test 3
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name3 = 0
    print('Test 3 : ',get_rating() ==name3)

    #Test 4
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name4 = 0
    print('Test 4 : ',get_rating() ==name4)

    #Test 5
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name5 = 0
    print('Test 5 : ',get_rating() ==name5)

def test_update_rating():
    """Fonction de test sur update_rating"""
    
    print("test_update_rating")
    #Test 0
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name0 = 0
    update_rating(name0)
    print('Test 0 : ',get_rating() ==name0)

    #Test 1
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name1 = 0
    update_rating(name1)
    print('Test 1 : ',get_rating() ==name1)

    #Test 2
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name2 = 0
    update_rating(name2)
    print('Test 2 : ',get_rating() ==name2)

    #Test 3
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name3 = 0
    update_rating(name3)
    print('Test 3 : ',get_rating() ==name3)

    #Test 4
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name4 = 0
    update_rating(name4)
    print('Test 4 : ',get_rating() ==name4)

    #Test 5
    Db.choix_de_la_data_base, Db.index_boisson = 0,0
    name5 = 0
    update_rating(name5)
    print('Test 5 : ',get_rating() ==name5)

if __name__ == '__main__':
    test = input("Tester les fonctions du script ? (0/1) : ")
    if test : 
        test_get_description_from_drink()
        test_get_description_from_drink()
        test_get_status_favory()
        test_update_status_favori()
        test_get_comment()
        test_update_comment()
        test_get_rating()
        test_update_rating()
    