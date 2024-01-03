import pandas
import csv

################################################################
################################################################
################################################################
#Fichier où on va créer les samples et extraire les éléments uniques 
#pour faire de l'autocomplétion sur les filtres 
################################################################
################################################################
################################################################

coffee = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/PROTO PYTHON/Raw_databases/coffee_analysis.csv")
#beers_samples = beers.head(100)
#beers_samples.to_csv("Samples/beers_samples.csv")

################################################################
#Extraction de chaque éléments pour les cafés
################################################################

#####
#Noms
#####

nbIng = 1

names = coffee['name']
names = names.drop_duplicates()


#####
#Toréfacteur
#####

roaster = coffee["roaster"]
roaster = roaster.drop_duplicates()

#####
#Toréfaction
#####

roast = coffee["roast"]
roast = roast.drop_duplicates()

#####
#Localisation
#####

country = coffee["loc_country"]
country = country.drop_duplicates()

#####
#Origine
#####

origins = coffee["origin_1"]
pandas.concat([origins, coffee["origin_2"]])
origins = origins.drop_duplicates()

#####
#Prix
#####

price = coffee["100g_USD"]
price = price.drop_duplicates()

#####
#Note 
#####

note = coffee["rating"]
note = note.drop_duplicates()




################################################################
#Création de la df
################################################################

data = {
    'Nom' : names,
    'Torefacteur' : roaster,
    'Torefaction': roast,
    'Pays': country,
    'Origine': origins,
    'Prix 100g': price,
    'Note': note
}

Uniques_elements = pandas.DataFrame(data)
Uniques_elements.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/coffee_unique_elements.csv")
