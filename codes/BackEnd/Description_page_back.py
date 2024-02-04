import Db_gestions as Db
import pandas as pd


def get_name_from_drink():
    db,index = Db.choix_de_la_data_base,Db.index_boisson
    boisson = Db.dbsall[db][0].iloc[index]
    name = boisson['Name']
    return name 

def get_description_from_drink():
    db,index = Db.choix_de_la_data_base,Db.index_boisson
    boisson = Db.dbsall[db][0].iloc[index]
    colonnes = Db.dbsall[db][0].columns
    text = ""
    columnns_to_avoid = []
    skip_next_iterations = False

    # Wines
    if Db.choix_de_la_data_base == 0:
        columns_to_avoid = ['Unnamed: 0','Name', 'PersonalRating', 'Favorite']
    # Cocktails
    elif Db.choix_de_la_data_base == 1: 
        columns_to_avoid = ['Unnamed: 0','Name', 'PersonalRating', 'Favorite', 'DrinkID', 'ModificationDate','IBA', 'Video']
    # Beers
    elif Db.choix_de_la_data_base == 2:
        columns_to_avoid = ['Unnamed: 0','Name', 'PersonalRating', 'Favorite', 'BeerID', 'BreweryID', 'BeerABV'] 
    # Coffees
    elif Db.choix_de_la_data_base == 3:
        columns_to_avoid = ['Unnamed: 0','Name', 'PersonalRating', 'Favorite'] 
    # Mocktails
    elif Db.choix_de_la_data_base == 4:
        columns_to_avoid = ['Unnamed: 0','Name', 'PersonalRating', 'Favorite']

    for i in range(len(boisson)) :
        if skip_next_iterations:
            break 

        colonne = colonnes[i]
        value = boisson[i]

        if colonne not in columns_to_avoid:
            if isinstance(value, list):
                value_str = ', '.join(str(item) for item in value)
            elif colonne == 'Price' and str(value) != 'Unfilled':
                if Db.choix_de_la_data_base == 0 : 
                    value_str = f"{value} $"
                elif Db.choix_de_la_data_base == 3: 
                    value_str = f"{value} $/100g"
            elif value not in ['',' ', 'nan']:
                value_str = str(value)
    
            if value_str.startswith('[') and value_str.endswith(']'):
                value_list = [item.strip("' ") for item in value_str[1:-1].split(',')]
                seen_elements = set()
                value_list_filtered = [item for item in value_list if item != 'nan' and item != '' and item != ' ' and (item not in seen_elements and seen_elements.add(item) is None)]
                value_str = ', '.join(value_list_filtered)
            
            text += str(colonne) + ' : ' + value_str + '\n' + '\n'

            if Db.choix_de_la_data_base == 2 and colonne == 'Style':
                text += "Rating (/5) : \n"
                
                for j in range(i+1, len(boisson)):
                    colonne = colonnes[j]
                    if colonne not in columns_to_avoid:
                        if colonne == 'ReviewsNumber':
                            text += '\n' + f"   - {str(colonne)} : {int(boisson[j]):,}" + '\n'
                        elif colonne != 'Comment':
                            text += '\n' + f"   - {str(colonne)} : {str(boisson[j])}" + '\n' 
                        else:
                            text += '\n' +  str(colonne) + ' : ' + str(boisson[j]) + '\n' + '\n'
                skip_next_iterations = True            
    return text
        
def get_status_favori():
    db,index =  Db.choix_de_la_data_base,Db.index_boisson
    favory = Db.dbsall[db][0].iloc[index][-1]
    return favory

def update_status_favori():
    db,index =  Db.choix_de_la_data_base, Db.index_boisson
    favory = not(Db.dbsall[db][0].iloc[index][-1])
    Db.dbsall[db][0].iloc[index,-1] = favory
    return favory

def get_comment():
    db,index =  Db.choix_de_la_data_base, Db.index_boisson
    comment = Db.dbsall[db][0].iloc[index][-2]
    if pd.isna(comment): return 'Leave a comment on the drink...'
    return comment

def update_comment(commentary):
    db,index =  Db.choix_de_la_data_base, Db.index_boisson
    Db.dbsall[db][0].iloc[index,-2] = commentary


def get_rating():
    db,index = Db.choix_de_la_data_base,  Db.index_boisson
    rating = Db.dbsall[db][0].iloc[index][-3]
    return rating

def update_rating(rating):
    db,index =  Db.choix_de_la_data_base,Db.index_boisson
    Db.dbsall[db][0].iloc[index,-3] = rating


    
'''if True : 
        # Wines
        if Db.choix_de_la_data_base == 0:
            real_names = ['country', 'description', 'price', 'province', 'variety', 'winery', 'region_']
            column_names = ['Provenance', 'Description', 'Prix', 'Province', 'Variété', 'Domaine', 'Région']
        # Cocktails
        elif Db.choix_de_la_data_base == 1: 
            real_names = ['strAlcoholic', 'strCategory', 'strDrinkThumb', 'strGlass', 'strIBA', 'strIngredient', 'strMeasure', 'strInstructions', 'strVideo']
            column_names = ['Type (Alcoholic/Non Alcoholic)', 'Catégorie', 'Lien Image Verre', 'Type de verre', 'strIBA', 'Ingrédients', 'Quantités', 'Préparation', 'Vidéo']
        # Beers
        elif Db.choix_de_la_data_base == 2: 
            real_names = ['brewery_name', 'beer_style', 'review_aroma', 'review_appearance', 'review_palate', 'review_taste', 'review_time','review_overall']
            column_names = ['Brasseur', 'Style', 'Arômes', 'Apparence', 'Palais', 'Goût', 'Nombre d''évaluations', 'Review globale']
        # Coffee
        elif Db.choix_de_la_data_base == 3: 
            real_names = ['loc_country', 'roaster', 'roast', '100g_USD', 'origin_', 'desc_', 'rating']
            column_names = ['Provenance', 'Torréfacteur', 'Torréfaction', 'Prix', 'Origine', 'Description', 'Note (/100)']
        # Mocktails
        elif Db.choix_de_la_data_base == 4:
            real_names = ['Ingredient ', 'Flavor Profile ', 'User Rating']
            column_names = ['Ingrédients', 'Saveurs', 'Note (/5)']

        #Création de la liste d'index pour récupérer les données
        for name in real_names:
                index = db_utilisee.columns.get_loc(name)
                column_index.append(index)

        #Récupération des données et mise en forme
        for i in range(len(column_index)):
            index = column_index[i]
            column_name = column_names[i]
            value = boisson[index]

            # Convertir la valeur en chaîne de caractères
            if isinstance(value, list):
                value_str = ', '.join(str(item) for item in value)
            elif column_name == 'Prix' and str(value) != 'nan':
                if Db.choix_de_la_data_base == 0 : 
                    value_str = f"{value} €"
                elif Db.choix_de_la_data_base == 3: 
                    value_str = f"{value} USD/100g"
            else:
                value_str = str(value)

            if value_str.startswith('[') and value_str.endswith(']'):
                value_list = [item.strip("' ") for item in value_str[1:-1].split(',')]
                seen_elements = set()
                value_list_filtered = [item for item in value_list if item != 'nan' and item != '' and item != ' ' and (item not in seen_elements and seen_elements.add(item) is None)]
                value_str = ', '.join(value_list_filtered)
            
            if Db.choix_de_la_data_base == 2 and column_name == 'Arômes':
                formatted_lines.append(f"Evaluations (/5) : ")
                remaining_elements = [col for col in column_names[i+1:]]
                for element in remaining_elements:
                    if element == 'Nombre d''évaluations':
                        formatted_lines.append(f"\n   - {element} : {int(boisson[column_index[column_names.index(element)]]):,}")
                    else :
                        formatted_lines.append(f"\n   - {element} : {boisson[column_index[column_names.index(element)]]:,}")
            elif column_name not in ['Apparence', 'Palais', 'Goût', 'Nombre d''évaluations', 'Review globale'] and value_str != 'nan'and value_str != '' and value_str != ' ':
                formatted_line = f"{column_name} : {value_str}"
                formatted_lines.append(formatted_line)
                formatted_lines.append('')

        return '\n'.join(formatted_lines)  '''  
    



#Je le garde dns un coin mais jsp si on le garde : 
