import pandas
import csv

################################################################
################################################################
################################################################
#Fichier où on va créer les samples et extraire les éléments uniques 
#pour faire de l'autocomplétion sur les filtres 
#Même question que pour biere
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

Cocktail0Name = mocktails['Cocktail Name']
Cocktail0Name = Cocktail0Name.drop_duplicates()

#####
#Ingredients
#####

Ingredient = mocktails["Ingredient 1"]
pandas.concat([Ingredient,mocktails["Ingredient 2"]])
pandas.concat([Ingredient,mocktails["Ingredient 3"]])
Ingredient = Ingredient.drop_duplicates()

#####
#Saveur
#####

Flavor0Profile = mocktails["Flavor Profile 1"]
pandas.concat([Flavor0Profile,mocktails["Flavor Profile 2"]])
Flavor0Profile = Flavor0Profile.drop_duplicates()

#####
#Note
#####

User0Rating = mocktails["User Rating"]
User0Rating = User0Rating.drop_duplicates()

######################################################
#Création de la df
################################################################

data = {
    'Cocktail Name' : Cocktail0Name,
    'Ingredient' : Ingredient,
    'Flavor Profile': Flavor0Profile,
    'User Rating': User0Rating,
}

Uniques_elements = pandas.DataFrame(data)
Uniques_elements.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/mocktail_unique_elements.csv")
