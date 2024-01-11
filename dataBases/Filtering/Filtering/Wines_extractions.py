import pandas
import csv
import re
################################################################
################################################################
################################################################
#Fichier où on va créer les samples et extraire les éléments uniques 
#pour faire de l'autocomplétion sur les filtres 
#Même question que bière
################################################################
################################################################
################################################################



try:
    wines = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/PROTO PYTHON/Raw_databases/winemag-data_first150k.csv")
    wines = wines.head(10)
except FileNotFoundError:
    print("Fichier pas présent sur l'ordinateur. Présent seulement en local sur l'odinateur de Pierre")

else :

    ##Sort les indices des colonnes en doubles 
    def trouver_indices(name_liste):
        indices_dict = {}
        for i, element in enumerate(name_liste):
            if element not in indices_dict:
                indices_dict[element] = []
            indices_dict[element].append(i)

        return [indices for indices in indices_dict.values() if len(indices) > 1]

    
    noms = wines.columns
    noms_colonnes = []
    for colonne in noms :
        noms_colonnes.append(re.sub(r'\d+', '', colonne))

    
    
    ##Concater les colonnes doubles et supprime les originaux (n'ajoue pas la colonne concaténée)
    def concatenation_creation():
        double_column = trouver_indices(noms_colonnes)
        colonnes_a_rajouter = []

        for colonnes_group in double_column :
            wines_new_column = pandas.concat([wines[wines.columns[index]] for index in colonnes_group])
            wines_new_column.reset_index()
            colonnes_a_rajouter.append(wines_new_column.drop_duplicates)

        wines['region_1'] = wines_new_column
        return wines
    
    def supprime_les_doublons():

        colonnes_a_rajouter = concatenation_creation()
        
        for colonne in wines.columns :
            colonnes_a_rajouter.append( wines[colonne].drop_duplicates())
            
        return pandas.DataFrame(colonnes_a_rajouter)

    print(concatenation_creation())
        


    ##Supprime tous 

     
    

        



    

    """uniques_elements = wines.copy()
    ##Suppressions des éléments en doubles 
    for column in uniques_elements.columns :
        print(column)
        uniques_elements[column] = uniques_elements[column] .drop_duplicates()

    uniques_elements.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/wines_unique_elements.csv")
"""
    ##Création des listes



"""

#wines_samples = wines.head(100)

# Ajouter une nouvelle colonne avec des valeurs nulles
#wines_samples['Favoris'] = None

#wines_samples.to_csv("Samples/wines_samples.csv")

################################################################
#Extraction de chaque pays pour les vins :
################################################################

#####
#Pays
#####

country = wines['country']
country = country.drop_duplicates()

#####
#Designation
#####

designation = wines["designation"]
designation = designation.drop_duplicates()

#####
#Points
#####

points = wines["points"]
points = points.drop_duplicates()

#####
#Prix
#####

price = wines["price"]
price = price.drop_duplicates()

#####
#Province
#####

province = wines["province"]
province = province.drop_duplicates()

#####
#Region
#####

region = wines['region_1']
pandas.concat([region,wines['region_2']])
region = region.drop_duplicates()

#####
#Variété
#####

variety = wines["variety"]
variety = variety.drop_duplicates()

#####
#vignoble
#####

winery = wines["winery"]
winery = winery.drop_duplicates()

#####
#Création de la df
#####

data = {
    'country' : country,
    'designation' : designation,
    'points': points,
    'price': price,
    'region': region,
    'variety' : variety,
    'winery' : winery
}

Uniques_elements = pandas.DataFrame(data)
Uniques_elements.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/wines_unique_elements.csv")
"""