import pandas

####################################
####################################
#Ouverture des BDD et créations des données filtrées pour l'autocomplétion etc
#J'ai pas trouvé le moyen d'ouvrir les colonnes avec des noms similaires (genre ingrédient1, ingrédient2 etc..)
####################################
####################################

#vins_unique_ingredients.drop("Unnamed: 0", axis=1, inplace=True)

########################################################################
########################################################################

Wines = pandas.read_csv('dataBases/Samples/wine_review_samples.csv')
Wines_elements_pertinents = ['winery','designation','price']
Wines_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/wines_unique_elements.csv')
Wines_uniques_elements.drop('Unnamed: 0', axis=1, inplace=True)

Wines_with_lists = Wines.copy()
Wines_with_lists["region"] = Wines_with_lists.apply(lambda row: [row['region_1'],row['region_2']],axis=1)
Wines_with_lists.drop('region_1', axis=1, inplace=True)
Wines_with_lists.drop('region_2', axis=1, inplace=True)

Wines_filters = Wines_with_lists[Wines_uniques_elements.columns]
###LA MISIONS : trouver les critères à afficher pour les df vs les critères à filtrer.

#Pas de listes à créer

########################################################################
########################################################################

Coffee = pandas.read_csv('dataBases/Samples/coffee_samples.csv')
Coffee_elements_pertinents = ['name','loc_country','rating']
Coffee_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/coffee_unique_elements.csv')
Coffee_uniques_elements.drop('Unnamed: 0', axis=1, inplace=True)
#les listes à créer sont origine et description
Coffee_with_lists = Coffee.copy()
Coffee_with_lists["origin"] = Coffee_with_lists.apply(lambda row: [row['origin_1'],row['origin_2']],axis=1)
Coffee_with_lists["description"] = Coffee_with_lists.apply(lambda row: [row['desc_1'],row['desc_2'],row['desc_3']],axis=1)

Coffee_with_lists.drop('origin_1', axis=1, inplace=True)
Coffee_with_lists.drop('origin_2', axis=1, inplace=True)
Coffee_with_lists.drop('desc_1', axis=1, inplace=True)
Coffee_with_lists.drop('desc_2', axis=1, inplace=True)
Coffee_with_lists.drop('desc_3', axis=1, inplace=True)

Coffee_filters = Coffee_with_lists[Coffee_uniques_elements.columns]



########################################################################
########################################################################

Cocktail = pandas.read_csv('dataBases/Samples/cocktail_samples.csv')
Cocktail_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/cocktail_unique_elements.csv')
Cocktail_uniques_elements.drop('Unnamed: 0', axis=1, inplace=True)
#Les listes à créer sont les ingrédients et les dosages
Cocktail_with_lists = Cocktail.copy()
Cocktail_with_lists['strIngredient'] = Cocktail_with_lists.apply(lambda row: [row[f'strIngredient{i}'] for i in range(1,16)], axis=1)
Cocktail_with_lists['strMeasure'] = Cocktail_with_lists.apply(lambda row: [row[f'strMeasure{i}'] for i in range(1,16)], axis=1)
for i in range(1,16) :
    Cocktail_with_lists.drop(f'strIngredient{i}', axis=1, inplace=True)
    Cocktail_with_lists.drop(f'strMeasure{i}', axis=1, inplace=True)

Cocktail_element_pertinent = ['strDrink','strCategory']
Cocktail_filters = Cocktail_with_lists[Cocktail_uniques_elements.columns]

########################################################################
########################################################################

Beers = pandas.read_csv('dataBases/Samples/beer_samples.csv')
Beers_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/beers_unique_elements.csv')
Beers_filters = Beers[Beers_uniques_elements.columns]
Beers_elements_pertinent = ['beer_name','brewery_name','beer_style']
#Pas de listes à créer

########################################################################
########################################################################
Mocktail = pandas.read_csv('dataBases/Samples/mocktail_samples.csv')
Mocktail_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/mocktail_unique_elements.csv')
#Les listes à créer sont les ingrédients et les gouts

Mocktail_with_lists = Mocktail.copy()
Mocktail_with_lists['Ingredient'] = Mocktail_with_lists.apply(lambda row: [row[f'Ingredient {i}'] for i in range(1,3)], axis=1)
Mocktail_with_lists['Flavor Profile'] = Mocktail_with_lists.apply(lambda row: [row[f'Flavor Profile {i}'] for i in range(1,2)], axis=1)
for i in range(1,2) :
    Mocktail_with_lists.drop(f'Ingredient {i}', axis=1, inplace=True)
    Mocktail_with_lists.drop(f'Flavor Profile {i}', axis=1, inplace=True)

Mocktail_filters = Mocktail_with_lists[Mocktail_uniques_elements.columns]
Mocktail_elements_pertinents = ['Cocktail Name','User Rating']

########################################################################
########################################################################


def choix_db(name):
    if name == 'Coffee' :
        return [Coffee,Coffee_filters,Coffee_uniques_elements,Coffee_elements_pertinents]
    elif name == 'Cocktail' :
        return [Cocktail,Cocktail_filters,Cocktail_uniques_elements,Cocktail_element_pertinent]
    elif name == 'Beers' :
        return [Beers,Beers_filters,Beers_uniques_elements,Beers_elements_pertinent]
    elif name == 'Mocktail' :
        return [Mocktail,Mocktail_filters,Mocktail_uniques_elements,Mocktail_elements_pertinents]
    else :
        return  [Wines,Wines_filters,Wines_uniques_elements,Wines_elements_pertinents]


