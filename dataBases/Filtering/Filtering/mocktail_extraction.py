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

mocktails = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/PROTO PYTHON/Raw_databases/moctail.csv")
#beers_samples = beers.head(100)
#beers_samples.to_csv("Samples/beers_samples.csv")

################################################################
#Extraction de chaque élément pour les mocktails :
################################################################

#####
#Names
#####

nbIng = 1

name = mocktails['Cocktail Name']
name = name.drop_duplicates()


#####
#Ingredients
#####

ingredients = mocktails["Ingredient 1"]
pandas.concat([ingredients,mocktails["Ingredient 2"]])
pandas.concat([ingredients,mocktails["Ingredient 3"]])
ingredients = ingredients.drop_duplicates()

#####
#Saveur
#####

saveur = mocktails["Flavor Profile 1"]
pandas.concat([saveur,mocktails["Flavor Profile 2"]])
saveur = saveur.drop_duplicates()

#####
#Note
#####

note = mocktails["User Rating"]
note = note.drop_duplicates()

######################################################
#Création de la df
################################################################

data = {
    'Noms' : name,
    'Ingredients' : ingredients,
    'Saveur': saveur,
    'Note ': note,
}

Uniques_elements = pandas.DataFrame(data)
Uniques_elements.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/mocktail_unique_elements.csv")
