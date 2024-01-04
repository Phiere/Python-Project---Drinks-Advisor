import pandas

####################################
####################################
#Ouverture des BDD et créations des données filtrées pour l'autocomplétion etc
#J'ai pas trouvé le moyen d'ouvrir les colonnes avec des noms similaires (genre ingrédient1, ingrédient2 etc..)
####################################
####################################

#vins_unique_ingredients.drop("Unnamed: 0", axis=1, inplace=True)

Wines = pandas.read_csv('dataBases/Samples/wine_review_samples.csv')
Wines_filters = Wines[['country','designation','points','price']]
Wines_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/wines_unique_elements.csv')

"""
Coffee = pandas.read_csv('dataBases/Samples/coffee_samples.csv')
Coffee_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/coffee_unique_elements.csv')
Coffee_filters = Coffee[Coffee_uniques_elements.columns]

Cocktail = pandas.read_csv('dataBases/Samples/cocktail_samples.csv')
Cocktail_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/cocktail_unique_elements.csv')
Cocktail_filters = Cocktail[Cocktail_uniques_elements.columns]

Beers = pandas.read_csv('dataBases/Samples/beer_samples.csv')
Beers_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/beers_unique_elements.csv')
Beers_filters = Beers[Beers_uniques_elements.columns]

Mocktail = pandas.read_csv('dataBases/Samples/mocktail_samples.csv')
Mocktail_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/mocktail_unique_elements.csv')
Mocktail_filters = Mocktail[Mocktail_uniques_elements.columns]
"""



