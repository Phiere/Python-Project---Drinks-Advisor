##############################
#Ce script contient les fonctions de back_end pour la création de l'écran création. Toutes
#les fonctions crées ici seront utilisées dans le script : Creation_page_UI.
##############################

import pandas as pd
import Db_gestions as Db
import random


def texte_vides(recovered_text):
    """Fonction permettant de vérifier si les entrées des nouvelles boissons sont vides et au bon format."""
    strInvalid = []
    numberInvalid = []
    for i,texte in enumerate(recovered_text) :
        if texte == 'numberFalse':
            numberInvalid.append(i)
        elif texte == 'strFalse':
            strInvalid.append(i)
    
    if numberInvalid:
        return 'numberFalse',numberInvalid 
    elif strInvalid:
        return 'strFalse',strInvalid
    else:
        return all(s == "" for s in recovered_text),None

def create_new_drink(recovered_text,recovered_names):
    """Créer une nouvelle ligne dans la data base choisie avec les informations complétées.
    
    - recovered_text : textes rentrés dans l'écran création
    - recovered_names : colonnes correspondantes aux textes rentrés 
    """
    data_base_index = Db.choix_de_la_data_base

    new_row = pd.Series() 
    Db.dbsall[data_base_index][0] = Db.dbsall[data_base_index][0]._append(new_row, ignore_index=True)

    new_index = len(Db.dbsall[data_base_index][0]) - 1
    Db.index_boisson = new_index

    for i in range(len(recovered_text)):
        texte = recovered_text[i]
        if texte == '' : texte = "Unfilled"
        colonne = recovered_names[i]

        try :
            texte = float(texte)
        except :
            if "," in texte :
                texte  = texte.split(",")

        
        Db.dbsall[data_base_index][0].at[new_index,colonne] = texte
   
    Db.dbsall[data_base_index][0].at[new_index,'PersonalRating'] = -1
    Db.dbsall[data_base_index][0].at[new_index,'Favorite'] = 0
    add_uniques_element(recovered_text,recovered_names)

def add_uniques_element(recovered_text,recovered_names):
    """Ajoute si nécessaire les éléments ajoutés dans le data_frame des éléments uniques"""
    data_base_index = Db.choix_de_la_data_base
    
    ## On rajoute toutes les nouvelles valeurs dans unique_element sans vérifier
    new_row = pd.Series() 
    Db.dbsall[data_base_index][1] = Db.dbsall[data_base_index][1]._append(new_row, ignore_index=True)
    new_index = len(Db.dbsall[data_base_index][1]) - 1      
    colomn_with_list_index = []

    for i in range(len(recovered_text)) :
        texte = recovered_text[i]
        if ',' in texte :
            colomn_with_list_index.append(i)
        else :
            colonne = recovered_names[i]
            Db.dbsall[Db.choix_de_la_data_base][1].at[new_index,colonne] = texte

    for index in colomn_with_list_index :
        texte_list = recovered_text[index]
        texte_list = texte_list.split(",")
        number_element = 1
        colonne = recovered_names[index]
        
        for texte in texte_list :

            Db.dbsall[Db.choix_de_la_data_base][1].at[new_index+number_element,colonne] = texte
            number_element +=1


    uniques_elements_columns_list = []

    for name in Db.dbsall[Db.choix_de_la_data_base][1].columns :
        uniques_elements_column = Db.dbsall[Db.choix_de_la_data_base][1][name].drop_duplicates()
        uniques_elements_columns_list.append(uniques_elements_column)

    new_unique_element = pd.DataFrame(dict(zip(Db.dbsall[Db.choix_de_la_data_base][1].columns,uniques_elements_columns_list)))

    Db.dbsall[Db.choix_de_la_data_base][1] = new_unique_element

########
#TEST
########
    
def test_text_vides(nb_test):
    """fonction de test pour la fonction test_text_vides"""
    print("Test_text_vides")
    
    for i in range(nb_test):
        index_db_rand = random.randint(0,4)
        db= Db.dbsall[index_db_rand][0]
        index_drink_rand = random.randint(0,len(db)-1)
        drink = db.loc[index_drink_rand]
        print(f"Test {i}")
        print("ligne db",drink)
        print("retour fonction",texte_vides(drink))

def test_create_new_drink(nb_test):
    """Test la fonction create_new_drink en comparant l'entrée de la fonction et la dernière ligne des data_base modifiée"""
    print("test_create_new_drink")

    for i in range(nb_test):
        index_db_rand = random.randint(0,4)
        db= Db.dbsall[index_db_rand][0]
        index_drink_rand = random.randint(0,len(db)-1)
        
        Db.choix_de_la_data_base = index_db_rand
        Db.index_boisson = index_drink_rand
        
def test_add_uniques_element():
    print("test_add_uniques_element")
    #Test 0
    test0,names0 = [],[]
    print("Test 0 :",test0,names0)
    add_uniques_element(test0,names0)
    print(texte_vides(test0))

    #Test 1
    test1,names1 = [],[]
    print("Test 0 :",test1,names1)
    add_uniques_element(test1,names1)
    print(texte_vides(test1))

    #Test 2
    test2,names2 = [],[]
    print("Test 0 :",test2,names2)
    add_uniques_element(test2,names2)
    print(texte_vides(test2))

if __name__ == '__main__':
    test = input("Tester les fonctions du script ? (0/1) : ")
    if test :
        test_text_vides(5)
        #test_create_new_drink()
        #test_add_uniques_element()
