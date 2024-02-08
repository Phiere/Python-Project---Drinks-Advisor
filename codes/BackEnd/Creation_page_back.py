import pandas as pd
import Db_gestions as Db

#V0.0
def texte_vides(get_text):
    textes_recuperees,_ = get_text()
    strInvalid = []
    numberInvalid = []
    for i,texte in enumerate(textes_recuperees) :
        if texte == 'numberFalse':
            numberInvalid.append(i)
        elif texte == 'strFalse':
            strInvalid.append(i)
    
    if numberInvalid:
        return 'numberFalse',numberInvalid 
    elif strInvalid:
        return 'strFalse',strInvalid
    else:
        return all(s == "" for s in textes_recuperees),None

#V0.1
def create_new_drink(get_text):
    """Créer un nouvelle ligne dans la data base choisie avec les informations complétées.
    
    - get_text : fonction de récupération des textes mis dans l'écran création"""
    data_base_index = Db.choix_de_la_data_base
    textes_recuperees,names = get_text()
    
    new_row = pd.Series() 
    Db.dbsall[data_base_index][0] = Db.dbsall[data_base_index][0]._append(new_row, ignore_index=True)

    new_index = len(Db.dbsall[data_base_index][0]) - 1
    Db.index_boisson = new_index

    for i in range(len(textes_recuperees)):
        texte = textes_recuperees[i]
        if texte == '' : texte = "Unfilled"
        colonne = names[i]

        try :
            texte = float(texte)
        except :
            if "," in texte :
                texte  = texte.split(",")

        
        Db.dbsall[data_base_index][0].at[new_index,colonne] = texte
   
    Db.dbsall[data_base_index][0].at[new_index,'PersonalRating'] = -1
    Db.dbsall[data_base_index][0].at[new_index,'Favorite'] = 0
    add_uniques_element(get_text=get_text)

#V0.1
def add_uniques_element(get_text):
    """Ajoute si nécessaire les éléments ajoutés dans le data_frame des éléments uniques"""
    textes_recuperees,names = get_text()
    data_base_index = Db.choix_de_la_data_base

    ## On rajoute toutes les nouvelles valeurs dans unique_element sans vérifier
    new_row = pd.Series() 
    Db.dbsall[data_base_index][1] = Db.dbsall[data_base_index][1]._append(new_row, ignore_index=True)
    new_index = len(Db.dbsall[data_base_index][1]) - 1      
    colomn_with_list_index = []

    for i in range(len(textes_recuperees)) :
        texte = textes_recuperees[i]
        if ',' in texte :
            colomn_with_list_index.append(i)
        else :
            colonne = names[i]
            Db.dbsall[Db.choix_de_la_data_base][1].at[new_index,colonne] = texte

    for index in colomn_with_list_index :
        texte_list = textes_recuperees[index]
        texte_list = texte_list.split(",")
        number_element = 1
        colonne = names[index]
        
        for texte in texte_list :

            Db.dbsall[Db.choix_de_la_data_base][1].at[new_index+number_element,colonne] = texte
            number_element +=1


    uniques_elements_columns_list = []

    for name in Db.dbsall[Db.choix_de_la_data_base][1].columns :
        uniques_elements_column = Db.dbsall[Db.choix_de_la_data_base][1][name].drop_duplicates()
        uniques_elements_columns_list.append(uniques_elements_column)

    new_unique_element = pd.DataFrame(dict(zip(Db.dbsall[Db.choix_de_la_data_base][1].columns,uniques_elements_columns_list)))



    Db.dbsall[Db.choix_de_la_data_base][1] = new_unique_element




