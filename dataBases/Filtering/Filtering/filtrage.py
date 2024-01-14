import pandas
import csv


# fabrication sample cocktail

#cocktail = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/PROTO PYTHON/Raw_databases/all_drinks.csv")
#cocktail_samples = cocktail.head(100)
'''
cocktail_samples = pandas.read_csv('dataBases/Samples/cocktail_samples.csv')
cocktail_samples['PersonalRating'] = None
cocktail_samples.to_csv("dataBases/Samples/cocktail_samples.csv")


# fabrication sample wine

"""
vin = pandas.read_csv('/Users/pierrehelas/Documents/IOGS/3A/Code/PROTO PYTHON/Raw_databases/winemag-data_first150k.csv')
# Supprimer la colonne "Unnamed: 0.1"
vin.drop("Unnamed: 0", axis=1, inplace=True)
print(vin.columns)
vin_sample = vin.head(100)
#print(vin_sample)
"""
vin_sample = pandas.read_csv('dataBases/Samples/wine_review_samples.csv')
vin_sample['PersonalRating'] = None
vin_sample.to_csv('dataBases/Samples/wine_review_samples.csv')

'''
# fabrication sample beer




vin = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/datasets/winemag-data_first150k.csv")
nouveau_noms_vin = {'designation': 'Name'}
vin.rename(columns=nouveau_noms_vin, inplace=True)
vin.to_csv("/Users/pierrehelas/Documents/IOGS/3A/datasets/winemag-data_first150k.csv")

cafe = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/datasets/coffee_analysis.csv")
nouveau_noms_cafe = {'name': 'Name'}
cafe.rename(columns=nouveau_noms_cafe, inplace=True)
cafe.to_csv("/Users/pierrehelas/Documents/IOGS/3A/datasets/coffee_analysis.csv")

cocktail = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/datasets/all_drinks.csv")
nouveau_noms_cocktail = {'strDrink': 'Name'}
cocktail.rename(columns=nouveau_noms_cocktail, inplace=True)
cocktail.to_csv("/Users/pierrehelas/Documents/IOGS/3A/datasets/all_drinks.csv")


mocktail = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/datasets/Mocktail_dataset.csv")
nouveau_noms_mocktail = {'Cocktail Name': 'Name'}
mocktail.rename(columns=nouveau_noms_mocktail, inplace=True)
mocktail.to_csv("/Users/pierrehelas/Documents/IOGS/3A/datasets/Mocktail_dataset.csv")



biere = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/datasets/beer_reviews.csv")

# Utilisez un dictionnaire pour mapper l'ancien nom au nouveau nom
nouveau_noms_bieres = {'beer_name': 'Name'}


biere.rename(columns=nouveau_noms_bieres, inplace=True)





biere = biere.sort_values('beer_beerid')

biere =  biere.drop_duplicates('beer_beerid')
biere_diff = biere.groupby('beer_beerid').mean('beer_abv')
biere_diff = biere_diff.round(2)
biere =  biere[['brewery_name','beer_style','Name','beer_beerid']]
biere = biere.merge(biere_diff,'inner',on = 'beer_beerid')


biere.to_csv("/Users/pierrehelas/Documents/IOGS/3A/datasets/beer_reviews.csv")

# fabrication sample coffee

'''coffee = pandas.read_csv('Raw_databases/coffee_analysis.csv')
coffee = coffee.head(100)
'''
'''coffee_samples = pandas.read_csv('dataBases/Samples/coffee_samples.csv')
coffee_samples['PersonalRating'] = None
coffee_samples.to_csv('dataBases/Samples/coffee_samples.csv')

######3 descriptions différentes ?

mocktail = pandas.read_csv('Raw_databases/moctail.csv')
mocktail = mocktail.head(100)

mocktail = pandas.read_csv('dataBases/Samples/mocktail_samples.csv')
mocktail['PersonalRating'] = None
mocktail.to_csv('dataBases/Samples/mocktail_samples.csv')


'''


#######################
####Extraction de chaque catégorie pour les vins :
#######################

"""
wines = pandas.read_csv("Raw_databases/winemag-data_first150k.csv")

'''pays = wines.drop_duplicates('country')
print(len(pays))
print(pays['country'])
'''
#####49 pays différents

localisation = wines.drop_duplicates('province')
print(len(localisation))
print(localisation['province'])

#####456 localisation différentes

region1 = wines.drop_duplicates('region_1')
print(len(region1))
print(region1['region_1'])

####1237 regions

region2 = wines.drop_duplicates('region_2')
print(len(region2))
print(region2['region_2'])

####19 regions

region1 = wines.drop_duplicates('variety')
print(len(region1))
print(region1['variety'])

####632 variété

region2 = wines.drop_duplicates('winery')
print(len(region2))
print(region2['winery'])

####14810 vignobles
"""
#######################
####Extraction de chaque catégorie pour les vins :
#######################




#########TEST ICI###########(pour voir si bien nettoyé)

