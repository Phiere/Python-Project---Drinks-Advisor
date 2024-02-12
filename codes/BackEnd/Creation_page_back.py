import pandas as pd
import Db_gestions as Db

#V0.1
def texte_vides(recovered_text):
    """Fonction permettant de vérifier si les entrées des nouvelles boisson sont vides et au bon format."""
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

#V0.2
def create_new_drink(recovered_text,recovered_names):
    """Créer un nouvelle ligne dans la data base choisie avec les informations complétées.
    
    - recovered_text : textes rentrés dans l'écran création
    - recovered_names : colonnes  correspondant aux textes rentrés 
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

#V0.1
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


####TEST
    
def test_text_vides():
    pass
    
def test_create_new_drink():
    """Test la fonction create_new_drink en comparant l'entrée de la fonction et la dernière ligne des data_base modifiée"""
    #Test vin
    Db.choix_de_la_data_base = 0
    texte0 = ["Us","Lovely","",54,54,"Supop","Supop","Supop","Supop",0,"",0]
    names0 = texte0,Db.dbsall[0][0].columns
    create_new_drink(texte0,names0)
    print("Test 0 : ",Db.dbsall[Db.choix_de_la_data_base][0].tail(1).list == texte0)

    #Test cocktails
    Db.choix_de_la_data_base = 1
    texte1,names1 = [],[]
    test_texte1 = texte1,names1
    create_new_drink()
    print("Test 1 : ",Db.dbsall[Db.choix_de_la_data_base][0].tail(1) == test_texte1)

    #Test café
    Db.choix_de_la_data_base = 2
    texte2,names2 = [],[]
    test_texte2 = texte2,names2
    create_new_drink()
    print("Test 2 : ",Db.dbsall[Db.choix_de_la_data_base][0].tail(1) == test_texte2)

    #Test bières
    Db.choix_de_la_data_base = 3
    texte3,names3 = [],[]
    test_texte3 = texte3,names3
    create_new_drink()
    print("Test 3 : ",Db.dbsall[Db.choix_de_la_data_base][0].tail(1) == test_texte3)

    #Test mocktails
    Db.choix_de_la_data_base = 4
    texte4,names4 = [],[]
    test_texte4 = texte4,names4
    create_new_drink()
    print("Test 4 : ",Db.dbsall[Db.choix_de_la_data_base][0].tail(1) == test_texte4)


def test_add_uniques_element():
    pass

if __name__ == '__main__':
    test = input("Tester les fonctions du script ? (0/1) : ")
    if test :
        test_text_vides()
        test_create_new_drink()
        test_add_uniques_element()
