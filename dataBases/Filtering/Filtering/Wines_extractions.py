import pandas
import csv

################################################################
################################################################
################################################################
#Fichier où on va créer les samples et extraire les éléments uniques 
#pour faire de l'autocomplétion sur les filtres 
#Même question que bière
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
points = points.astype(int)
#####
#Prix
#####

price = wines["price"]
price = price.drop_duplicates()

price.fillna(0, inplace=True)
price = price.astype(int)

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

Uniques_elements['price'].fillna(-1, inplace=True)
Uniques_elements['price'] = Uniques_elements['price'].astype(int)
Uniques_elements['points'].fillna(-1, inplace=True)
Uniques_elements['points'] = Uniques_elements['points'].astype(int)

Uniques_elements.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/wines_unique_elements.csv")
