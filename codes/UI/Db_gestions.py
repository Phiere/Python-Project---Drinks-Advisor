import pandas

####################################
####################################
#Ouverture des BDD et créations des données filtrées pour l'autocomplétion etc
#Pour les colonnes en 'double' : Ingrédient1, ingrédient2,... On va créer des listes
####################################
####################################

#vins_unique_ingredients.drop("Unnamed: 0", axis=1, inplace=True)

########################################################################
########################################################################

Wines = pandas.read_csv('dataBases/Samples/wine_review_samples.csv')
Wines_filters = Wines[['country','designation','points','price']]
Wines_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/wines_unique_elements.csv')
#Pas de listes à créer

########################################################################
########################################################################

Coffee = pandas.read_csv('dataBases/Samples/coffee_samples.csv')
Coffee_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/coffee_unique_elements.csv')
Coffee_uniques_elements.drop('Unnamed: 0', axis=1, inplace=True)
#les listes à créer sont origine et description
Coffee_with_lists = Coffee.copy()
Coffee_with_lists["originlist2"] = Coffee_with_lists.apply(lambda row: [row['origin_1'],row['origin_2']],axis=1)
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
Cocktail_with_lists['strIngredientlist15'] = Cocktail_with_lists.apply(lambda row: [row[f'strIngredient{i}'] for i in range(1,16)], axis=1)
Cocktail_with_lists['strMeasure'] = Cocktail_with_lists.apply(lambda row: [row[f'strMeasure{i}'] for i in range(1,16)], axis=1)
for i in range(1,16) :
    Cocktail_with_lists.drop(f'strIngredient{i}', axis=1, inplace=True)
    Cocktail_with_lists.drop(f'strMeasure{i}', axis=1, inplace=True)


Cocktail_filters = Cocktail_with_lists[Cocktail_uniques_elements.columns]

########################################################################
########################################################################

Beers = pandas.read_csv('dataBases/Samples/beer_samples.csv')
Beers_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/beers_unique_elements.csv')
Beers_uniques_elements.drop('Unnamed: 0', axis=1, inplace=True)
Beers_filters = Beers[Beers_uniques_elements.columns]

#Pas de listes à créer

########################################################################
########################################################################

Mocktail = pandas.read_csv('dataBases/Samples/mocktail_samples.csv')
Mocktail_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/mocktail_unique_elements.csv')
#Les listes à créer sont les ingrédients et les gouts
Mocktail_uniques_elements.drop('Unnamed: 0', axis=1, inplace=True)

Mocktail_with_lists = Mocktail.copy()
Mocktail_with_lists['Ingredientlist3'] = Mocktail_with_lists.apply(lambda row: [row[f'Ingredient {i}'] for i in range(1,3)], axis=1)
Mocktail_with_lists['Flavor Profilelist2'] = Mocktail_with_lists.apply(lambda row: [row[f'Flavor Profile {i}'] for i in range(1,2)], axis=1)
for i in range(1,2) :
    Mocktail_with_lists.drop(f'Ingredient {i}', axis=1, inplace=True)
    Mocktail_with_lists.drop(f'Flavor Profile {i}', axis=1, inplace=True)

Mocktail_filters = Mocktail_with_lists[Mocktail_uniques_elements.columns]

########################################################################
########################################################################


def choix_db(name):
    if name == 'Coffee' :
        return [Coffee,Coffee_filters,Coffee_uniques_elements]
    elif name == 'Cocktail' :
        return [Cocktail,Cocktail_filters,Cocktail_uniques_elements]
    elif name == 'Beers' :
        return [Beers,Beers_filters,Beers_uniques_elements]
    elif name == 'Mocktail' :
        return [Mocktail,Mocktail_filters,Mocktail_uniques_elements]
    else :
        return  [Wines,Wines_filters,Wines_uniques_elements]


