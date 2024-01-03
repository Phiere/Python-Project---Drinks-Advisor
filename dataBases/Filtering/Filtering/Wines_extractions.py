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

wines = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/PROTO PYTHON/Raw_databases/winemag-data_first150k.csv")
#wines_samples = wines.head(100)
#wines_samples.to_csv("Samples/wines_samples.csv")

################################################################
#Extraction de chaque pays pour les vins :
################################################################

#####
#Pays
#####

nbIng = 1

pays = wines['country']
pays = pays.drop_duplicates()


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

prix = wines["price"]
prix = prix.drop_duplicates()

#####
#Province
#####

province = wines["province"]
province = province.drop_duplicates()

#####
#Region
#####

regions = wines['region_1']
pandas.concat([regions,wines['region_2']])
regions = regions.drop_duplicates()

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
    'Pays' : pays,
    'Designation' : designation,
    'Points': points,
    'Prix': prix,
    'Region': regions,
    'Variete' : variety,
    'Vignoble' : winery
}

Uniques_elements = pandas.DataFrame(data)
Uniques_elements.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/wines_unique_elements.csv")