import pandas
import csv

################################################################
################################################################
################################################################
#Fichier où on va créer les samples et extraire les éléments uniques 
#pour faire de l'autocomplétion sur les filtres 
#Même questions que pour beer
################################################################
################################################################
################################################################

coffee = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/PROTO PYTHON/Raw_databases/coffee_analysis.csv")
#coffee_samples = beers.head(100)
#coffee_samples.to_csv("Samples/coffee_samples.csv")

################################################################
#Extraction de chaque éléments pour les cafés
################################################################

#####
#Noms
#####

name = coffee['name']
name = name.drop_duplicates()

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

loc_country = coffee["loc_country"]
loc_country = loc_country.drop_duplicates()

#####
#Origine
#####

origin_ = coffee["origin_1"]
pandas.concat([origin_, coffee["origin_2"]])
origin_ = origin_.drop_duplicates()

#####
#Prix
#####

a100g_USD = coffee["100g_USD"]
a100g_USD = a100g_USD.drop_duplicates()

#####
#Note 
#####

rating = coffee["rating"]
rating = rating.drop_duplicates()

################################################################
#Création de la df
################################################################

data = {
    'name' : name,
    'roaster' : roaster,
    'roast': roast,
    'loc_country': loc_country,
    'origin': origin_,
    '100g_USD': a100g_USD,
    'rating': rating
}

Uniques_elements = pandas.DataFrame(data)
Uniques_elements.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/coffee_unique_elements.csv")
