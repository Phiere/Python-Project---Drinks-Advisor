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

cocktail = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/PROTO PYTHON/Raw_databases/all_drinks.csv")
#cocktail_samples = cocktail.head(100)
#cocktail_samples.to_csv("Samples/cocktail_samples.csv")

################################################################
#Extraction de chaque catégorie pour les cocktails :
################################################################

################################################################
#Ingrédients
################################################################

nbIng = 15
ingredients = cocktail.drop_duplicates("strIngredient1")
ingredients = ingredients['strIngredient1']
for i in range(2,nbIng+1):
    temp = cocktail.drop_duplicates(f"strIngredient{i}")
    pandas.concat([ingredients,temp[f"strIngredient{i}"]])

ingredients = ingredients.drop_duplicates()
#print(ingredients)

#####
#Exctraction de tous les noms différents pour l'autocomplétion
#####

nbnames = 1
names = cocktail["strDrink"]
names = names.drop_duplicates()

#print(names)

#####
#Exctraction des Catégories
#####

nbnames = 1
categories = cocktail["strCategory"]
categories = categories.drop_duplicates()

#print(categories)

#####
#Exctraction des verres
#####

nbnames = 1
verres = cocktail["strGlass"]
verres = verres.drop_duplicates()

#print(verres)

#####
#Création de la df
#####

data = {
    'Ingredients': ingredients,
    'Name': names,
    'Categorie': categories,
    'Verres' : verres
}

Uniques_elements = pandas.DataFrame(data)
Uniques_elements.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/cocktail_unique_elements.csv")
