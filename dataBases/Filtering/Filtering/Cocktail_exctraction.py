import pandas
import csv

################################################################
################################################################
################################################################
#Fichier où on va créer les samples et extraire les éléments uniques 
#pour faire de l'autocomplétion sur les filtres 
#Mêmes questions que pour les bières
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
strIngredient = cocktail.drop_duplicates("strIngredient1")
strIngredient = strIngredient['strIngredient1']
for i in range(2,nbIng+1):
    temp = cocktail.drop_duplicates(f"strIngredient{i}")
    pandas.concat([strIngredient,temp[f"strIngredient{i}"]])

ingredients = strIngredient.drop_duplicates()
#print(ingredients)

#####
#Noms
#####

strDrink = cocktail["strDrink"]
strDrink = strDrink.drop_duplicates()

#####
#Catégories
#####

strCategory = cocktail["strCategory"]
strCategory = strCategory.drop_duplicates()

#####
#Verres
#####

strGlass = cocktail["strGlass"]
strGlass = strGlass.drop_duplicates()

#####
#Création de la df
#####

data = {
    'strIngredientlist15': strIngredient,
    'strDrink': strDrink,
    'strCategory': strCategory,
    'strGlass' : strGlass
}

Uniques_elements = pandas.DataFrame(data)
Uniques_elements.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/cocktail_unique_elements.csv")
