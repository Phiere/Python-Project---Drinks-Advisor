import pandas
import csv


# fabrication sample cocktail
'''
cocktail = pandas.read_csv("all_drinks.csv")
cocktail_samples = cocktail.head(100)
cocktail_samples.to_csv("Samples/cocktail_samples.csv")
'''

# fabrication sample wine

'''vin = pandas.read_csv('winemag-data_first150k.csv')
vin_sample = vin.head(100)
vin_sample.to_csv('Samples/wine_review_samples.csv')
'''

# fabrication sample beer

'''
biere = pandas.read_csv('beer_reviews.csv')
biere = biere.sort_values('beer_beerid')

biere =  biere.drop_duplicates('beer_beerid')
biere_diff = biere.groupby('beer_beerid').mean('beer_abv')
biere_diff = biere_diff.round(2)
biere =  biere[['brewery_name','beer_style','beer_name','beer_beerid']]
biere = biere.merge(biere_diff,'inner',on = 'beer_beerid')

beer_samples = biere.head(100)
beer_samples.to_csv('Samples/beer_samples.csv')
'''

# fabrication sample coffee

'''coffee = pandas.read_csv('Raw_databases/coffee_analysis.csv')
coffee = coffee.head(100)
coffee.to_csv('Samples/coffee_samples.csv')
'''
######3 descriptions différentes ?

'''
mocktail = pandas.read_csv('Raw_databases/moctail.csv')
mocktail = mocktail.head(100)
mocktail.to_csv('Samples/mocktail_samples.csv')
'''

#  Extraction de chaque catégorie pour les cocktails :


#cocktail = pandas.read_csv("Raw_databases/all_drinks.csv")

# déjà les 'catégories'
#temp = cocktail.drop_duplicates('strCategory')
#print(temp['strCategory'])
#### Ici on devrait peur être séparer juste shot et cocktail ? Pcq toute les
#### autres catégories pour moi ça reste des cocktails

#ensuite les ingrédients
'''nbIng = 15
ingredients = cocktail.drop_duplicates("strIngredient1")
ingredients = ingredients['strIngredient1']
for i in range(2,nbIng+1):
    temp = cocktail.drop_duplicates(f"strIngredient{i}")
    pandas.concat([ingredients,temp[f"strIngredient{i}"]])


ingredients = ingredients.drop_duplicates()
print(ingredients)
ingredients.to_csv('items_for_filtering/ingredients.csv')'''
#La on est sur 540 différents, on fait un truc en auto complétion ? Ou alors on 
#décompose selon plusieurs catégorie ? (alcool, pas alcool)
#j'ai rempli un fichier avec alcool/pas alcool pour chaque ingrédieent


#######################
####Extraction de chaque catégorie pour les vins :
#######################

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

#######################
####Extraction de chaque catégorie pour les vins :
#######################




#########TEST ICI###########(pour voir si bien nettoyé)

