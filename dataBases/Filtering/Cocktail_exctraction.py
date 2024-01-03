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
'''
nbIng = 15
ingredients = cocktail.drop_duplicates("strIngredient1")
ingredients = ingredients['strIngredient1']
for i in range(2,nbIng+1):
    temp = cocktail.drop_duplicates(f"strIngredient{i}")
    pandas.concat([ingredients,temp[f"strIngredient{i}"]])

ingredients = ingredients.drop_duplicates()
print(ingredients)
ingredients.to_csv('items_for_filtering/ingredients.csv')
'''


#####
#Exctraction de tous les noms différents pour l'autocomplétion
#####
nbnames = 1
names = cocktail["strDrink"]
names = names.drop_duplicates()

print(names)
