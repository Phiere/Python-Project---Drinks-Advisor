import pandas
import csv
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
# - Attention : lors de rajout d'une nouvelle data_frame, il est préférable de modifier à la main le nom des colonnes afin d'un affichage plus agréable.
################################################################
################################################################
################################################################

raw_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/Code/PROTO PYTHON/Raw_databases/winemag-data_first150k.csv"
listed_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/tests.csv"
uniques_element_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/tests.csv"

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
        data_base['Commentary'] = ''
        data_base['Favories'] = ''
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
            uniques_elements_column = data_base[name_column_wo_twin].drop_duplicates()
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
    
def raw_data_traitement(raw_data_frame_path,listed_data_frame_path,uniques_element_data_frame_path):
        
        try:
            raw_data_frame = pandas.read_csv(raw_data_frame_path)
            raw_data_frame = raw_data_frame.head(100)
        except FileNotFoundError:
            print("Fichier pas présent sur l'ordinateur. Présent seulement en local sur l'odinateur de Pierre")

        else :
            #Applique l'ensemble des traitements nécessaire à l'utilisation des data_bases
            listed_doubles_columns = creation_list_colonnes_doubles(raw_data_frame)
            listed_doubles_columns.to_csv(listed_data_frame_path)

            uniques_elements_data_frame = creation_unique_elements_data_frame(raw_data_frame)
            uniques_elements_data_frame.to_csv(uniques_element_data_frame_path)

    #Attention à modifier les noms des colonnes de la database listed


################################################################
################################################################
################################################################
#Mise en application sur les databases choisies
################################################################
################################################################
################################################################

#Attention à ne pas décommenter ces test, ils doivent seulement être fait une fois.


wines_raw_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/datasets/winemag-data_first150k.csv"
wines_listed_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Samples/wines_samples.csv"
wines_uniques_element_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/wines_unique_elements.csv"

coffees_raw_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/datasets/coffee_analysis.csv"
coffees_listed_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Samples/coffee_samples.csv"
coffees_uniques_element_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/coffee_unique_elements.csv"

cocktails_raw_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/datasets/all_drinks.csv"
cocktails_listed_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Samples/cocktails_samples.csv"
cocktails_uniques_element_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/cocktail_unique_elements.csv"

mocktails_raw_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/datasets/Mocktail_dataset.csv"
mocktails_listed_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Samples/mocktail_samples.csv"
mocktails_uniques_element_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/mocktail_unique_elements.csv"

beers_raw_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/datasets/beer_reviews.csv"
beers_listed_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Samples/beer_samples.csv"
beers_uniques_element_data_frame_path = "/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/beers_unique_elements.csv"

if __name__ == '__main__':

    raw_data_traitement(wines_raw_data_frame_path,wines_listed_data_frame_path,wines_uniques_element_data_frame_path)
    raw_data_traitement(coffees_raw_data_frame_path,coffees_listed_data_frame_path,coffees_uniques_element_data_frame_path)
    raw_data_traitement(cocktails_raw_data_frame_path,cocktails_listed_data_frame_path,cocktails_uniques_element_data_frame_path)
    raw_data_traitement(mocktails_raw_data_frame_path,mocktails_listed_data_frame_path,mocktails_uniques_element_data_frame_path)
    raw_data_traitement(beers_raw_data_frame_path,beers_listed_data_frame_path,beers_uniques_element_data_frame_path)
