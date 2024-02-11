import pandas
import re
################################################################
################################################################
################################################################
#Dans ce script on va procéder à plusieurs traitements sur les data-bases. Ces traitements ne sont oppérer qu'une fois et on 
#utilisera par la suite les data_frame créées dans notre logiciel. Si l'on souhaite rajouter une data base dans notre logiciel,
#il faudra relancer ce script en complétant les chemins des fichiers.
# Etapes :
# - Renseigner les chemins de départ et d'arrivé des différentes Data_Frame (voir ....)
# - Traitement 1 : remplace les colonnes doubles : (ingrédient1, ingrédient2,...) par uen colonne contenant la liste des éléments ([ingrédient1, ingrédient2])
# - Traitement 2 : normalise les éléments dans une même colonne : (Vodka , vodka --> vodka).
# - Traitement 3 : rajouter à chaque data_base les colonnes notes_personnelle, commentary, favories
# - Traitement 4 : changer les nan
# - Traitemetn 5 : enlever les colonnes intutiles (dépalcer en 1)
# - Attention : lors de rajout d'une nouvelle data_frame, il est préférable de modifier à la main le nom des colonnes afin d'un affichage plus agréable.
################################################################
################################################################
################################################################

def trouver_indices(df_columns_names):
        # Sort les indices des colonnes en doubles, i.e des colonnes avec le même noms (une fois leur caractères non str enlevés)

        noms_colonnes = []
        for colonne in df_columns_names :
            noms_colonnes.append(re.sub(r'\d+', '', colonne))

        indices_dict = {}
        for i, element in enumerate(noms_colonnes):
            if element not in indices_dict:
                indices_dict[element] = []
            indices_dict[element].append(i)

        return [indices for indices in indices_dict.values() if len(indices) > 1]

def liste_columns_names(data_base):
        noms_colonnes = []
        for name in data_base:
            noms_colonnes.append(name)
        return noms_colonnes
    
def creation_list_colonnes_doubles(data_base):
        #Créer le clone de la data_frame en entreé en changeant les colonnes jumelles par une colonne avec une liste de leurs éléments

        liste_colonnes_doubles = trouver_indices(data_base.columns)

        for colonnes_doubles in liste_colonnes_doubles :
            name_colonne = re.sub(r'\d+', '', data_base.columns[colonnes_doubles[0]])
            data_base[name_colonne] = data_base.apply(lambda row: [row[data_base.columns[i]] for i in colonnes_doubles], axis=1)

        liste_colonnes_doubles_flated = [element for sous_liste in liste_colonnes_doubles for element in sous_liste]
        data_base = data_base.drop(data_base.columns[liste_colonnes_doubles_flated],axis=1)

        data_base['PersonalRating'] = '-1'
        data_base['Commentary'] = 'Unfilled'
        data_base['Favories'] = '0'
        return data_base
    
    #Améliorer les compréhensions de listes
    #Contrairement aux autres fonctions, cette fonction sera appelée ailleurs pour créer les liste pour l'autocomplétion

def creation_unique_elements_data_frame(data_base):

        #Cette fonction créer un clone de la database en entrée en supprimant tous les éléments en doublons pour ne garder que les éléments
        #uniques pour chaque colonne. Utile pour l'auto complétion.

        liste_colonnes_doubles = trouver_indices(data_base.columns)

        columns_names_with_twin = liste_columns_names(data_base)
        
    
        liste_colonnes_doubles_flated = [element for sous_liste in liste_colonnes_doubles for element in sous_liste]
        columns_names_without_twin =  [columns_names_with_twin[i] for i in range(len(columns_names_with_twin)) if i not in liste_colonnes_doubles_flated]


        
        
        #Creation des colonnes sans répétitions
        uniques_elements_columns_list = []

        for name_column_wo_twin in columns_names_without_twin :
            
            uniques_elements_column = data_base[name_column_wo_twin]
            uniques_elements_column = uniques_elements_column.apply(lambda x: ' '.join(word.capitalize() for word in x.split()) if (isinstance(x, str)) else x)
            uniques_elements_column = uniques_elements_column.drop_duplicates()
            uniques_elements_columns_list.append(uniques_elements_column)


        #Rajout des jumeaux fusionnés
            
        for indexes in liste_colonnes_doubles :
            name_new_column = re.sub(r'\d+', '', columns_names_with_twin[indexes[0]])
            columns_names_without_twin.append(name_new_column)

        for indexes in liste_colonnes_doubles :
            twin_columns = []
            for index in indexes:
                twin_columns.append(data_base[columns_names_with_twin[index]])
            uniques_elements_column = pandas.concat(twin_columns)

            uniques_elements_column = uniques_elements_column.reset_index(drop=True)
            
            uniques_elements_column = uniques_elements_column.drop_duplicates()
            uniques_elements_columns_list.append(uniques_elements_column)

        return pandas.DataFrame(dict(zip(columns_names_without_twin,uniques_elements_columns_list)))

def suppression_unnamed(data_base):
     liste_columns_nuisibles = [element for element in data_base.columns if "Unnamed" in element]
     return data_base.drop(liste_columns_nuisibles,axis = 1)

def normalise_str(data_base):
    columns = data_base.columns
    for column in columns :
        data_base[column] = data_base[column].apply(lambda x: ' '.join(word.capitalize() for word in x.split()) if (isinstance(x, str)) else x) 
    return data_base

def changer_nan(db):
    tipes = db.dtypes
    colonnes = db.columns
    for i in range(len(db.dtypes)) :
        tipe = tipes[i]
        if tipe == float or tipe == int :
            db[colonnes[i]] = db[colonnes[i]].fillna(-1)
        else :
            db[colonnes[i]] = db[colonnes[i]].fillna("Unfilled")
    return db

def delete_unnecessary_column(data_frame,unnecessary_column):
     for column in unnecessary_column :
          data_frame.drop(column, axis=1, inplace=True)
     
def raw_data_traitement(raw_data_frame_path,listed_data_frame_path,uniques_element_data_frame_path,unnecessary_column,new_column_names):
        
        try:
            raw_data_frame = pandas.read_csv(raw_data_frame_path)
            raw_data_frame = raw_data_frame.head(100)
        except FileNotFoundError:
            print("Fichier pas présent sur l'ordinateur. Présent seulement en local sur l'odinateur de Pierre")

        else :

            delete_unnecessary_column(raw_data_frame,unnecessary_column)  

            raw_data_frame = changer_nan(raw_data_frame)
            raw_data_frame = normalise_str(raw_data_frame)
            listed_doubles_columns = creation_list_colonnes_doubles(raw_data_frame)
            listed_doubles_columns = suppression_unnamed(listed_doubles_columns)
            listed_doubles_columns = listed_doubles_columns.rename(columns=new_column_names)
            listed_doubles_columns.to_csv(listed_data_frame_path)
        

            uniques_elements_data_frame = creation_unique_elements_data_frame(raw_data_frame)
            uniques_elements_data_frame = suppression_unnamed(uniques_elements_data_frame)
            uniques_elements_data_frame = uniques_elements_data_frame.rename(columns=new_column_names)
            uniques_elements_data_frame.to_csv(uniques_element_data_frame_path)

    #Attention à modifier les noms des colonnes de la database listed


################################################################
################################################################
################################################################
#Mise en application sur les databases choisies
################################################################
################################################################
################################################################


wines_raw_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/SignalImage/ProjetPython/datasets/winemag-data_first150k.csv"
wines_listed_data_frame_path = "dataBases/Samples/wines_samples.csv"
wines_uniques_element_data_frame_path = "dataBases/Filtering/Uniques_elements/wines_unique_elements.csv"
wines_unnecessary_columns = []
wines_new_column_names = {'country' : 'Country', 'description' : 'Description', 'points' : 'Points', 
                        'price' : 'Price', 'province' : 'Province', 'variety' : 'Variety', 'winery' : 'Winery', 
                        'region_' : 'Region', 'Commentary' : 'Comment', 'Favories' : 'Favorite'}


coffees_raw_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/SignalImage/ProjetPython/datasets/coffee_analysis.csv"
coffees_listed_data_frame_path = "dataBases/Samples/coffee_samples.csv"
coffees_uniques_element_data_frame_path = "dataBases/Filtering/Uniques_elements/coffee_unique_elements.csv"
coffees_unnecessary_columns = ['review_date']
coffee_new_column_names = {'roaster' : 'Roaster', 'roast' : 'Roast', 'loc_country' : 'Country', 
                        '100g_USD' : 'Price', 'rating' : 'UserRating', 'origin_' : 'Origin', 
                        'desc_' : 'Description', 'Commentary' : 'Comment', 'Favories' : 'Favorite'}


cocktails_raw_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/SignalImage/ProjetPython/datasets/all_drinks.csv"
cocktails_listed_data_frame_path = "dataBases/Samples/cocktails_samples.csv"
cocktails_uniques_element_data_frame_path = "dataBases/Filtering/Uniques_elements/cocktail_unique_elements.csv"
cocktails_unnecessary_columns = ['dateModified','idDrink','strDrinkThumb','strVideo']
cocktails_new_column_names = {'strAlcoholic' : 'DrinkType', 
                        'strCategory' : 'Category', 'strGlass' : 'Glass', 'strIBA' : 'IBA', 'strInstructions' : 'Recipe', 
                        'strIngredient' : 'Ingredients', 'strMeasure' : 'Measure', 'Commentary' : 'Comment', 'Favories' : 'Favorite'}

mocktails_raw_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/SignalImage/ProjetPython/datasets/Mocktail_dataset.csv"
mocktails_listed_data_frame_path = "dataBases/Samples/mocktail_samples.csv"
mocktails_uniques_element_data_frame_path = "dataBases/Filtering/Uniques_elements/mocktail_unique_elements.csv"
mocktails_unnecessary_columns = []
mocktails_new_column_names = {'User Rating' : 'UserRating', 'Ingredient ' : 'Ingredients', 'Flavor Profile ' : 'FlavorProfile', 
                        'Commentary' : 'Comment', 'Favories' : 'Favorite'}

beers_raw_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/SignalImage/ProjetPython/datasets/beer_reviews.csv"
beers_listed_data_frame_path = "dataBases/Samples/beer_samples.csv"
beers_uniques_element_data_frame_path = "dataBases/Filtering/Uniques_elements/beers_unique_elements.csv"
beers_unnecessary_columns = ['beer_beerid','brewery_id']
beers_new_column_names = {'brewery_name' : 'Brewery', 'beer_style' : 'Style', 
                        'review_time' : 'ReviewsNumber', 'review_overall' : 'OverallReview',
                        'review_aroma' : 'Aroma', 'review_appearance' : 'Appearance', 'review_palate' : 'Palate', 'review_taste' : 'Taste', 
                        'beer_abv' : 'BeerABV','Commentary' : 'Comment', 'Favories' : 'Favorite'}

if __name__ == '__main__':
    input = "Relancer ce script réinitialise les data_base, continuer ? (0/1) : "
    raw_data_traitement(wines_raw_data_frame_path,wines_listed_data_frame_path,wines_uniques_element_data_frame_path,wines_unnecessary_columns,wines_new_column_names)
    raw_data_traitement(coffees_raw_data_frame_path,coffees_listed_data_frame_path,coffees_uniques_element_data_frame_path,coffees_unnecessary_columns,coffee_new_column_names)
    raw_data_traitement(cocktails_raw_data_frame_path,cocktails_listed_data_frame_path,cocktails_uniques_element_data_frame_path,cocktails_unnecessary_columns,cocktails_new_column_names)
    raw_data_traitement(mocktails_raw_data_frame_path,mocktails_listed_data_frame_path,mocktails_uniques_element_data_frame_path,mocktails_unnecessary_columns,mocktails_new_column_names)
    raw_data_traitement(beers_raw_data_frame_path,beers_listed_data_frame_path,beers_uniques_element_data_frame_path,beers_unnecessary_columns,beers_new_column_names)
