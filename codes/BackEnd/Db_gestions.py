import pandas

####################################
####################################
#Ouverture des BDD et créations des données filtrées pour l'autocomplétion etc
#Strcuture des fonctions :
#  ..._cleaned : Databases nettoyées et sous forme de liste pour les colonnes doubles. Contiennent toutes les données
#  ..._pertinents_elements : Liste des colonnes qui serviront de filtres pour la recherche
#  ..._unique_elements : Database des éléments uniques de toutes les colonnes
#  ..._filters : Datanse des éléments uniques pour les filtres de l'autocomplétion
####################################
####################################

def initialisationWine():

    ## Appels des databases préalablement nettoyées
    wines_cleaned = pandas.read_csv('dataBases/Samples/wines_samples.csv')
    wines_pertinents_elements = ['Unnamed: 0','winery','Name','price']
    wines_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/wines_unique_elements.csv')
    wines_filters = wines_cleaned[wines_uniques_elements.columns]

    return [wines_cleaned,wines_filters,wines_uniques_elements,wines_pertinents_elements]

def initilisationCoffee():

    ##
    coffee_cleaned = pandas.read_csv('dataBases/Samples/coffee_samples.csv')
    coffee_elements_pertinents = ['Unnamed: 0','Name','loc_country','rating']
    coffee_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/coffee_unique_elements.csv')
    coffee_filters = coffee_cleaned[coffee_uniques_elements.columns]

    return [coffee_cleaned,coffee_filters,coffee_uniques_elements,coffee_elements_pertinents]

def initilisationCocktail():

    ##
    cocktail_cleaned = pandas.read_csv('dataBases/Samples/cocktails_samples.csv')
    cocktail_element_pertinent = ['Unnamed: 0','Name','strCategory']
    cocktail_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/cocktail_unique_elements.csv')
    cocktail_filters = cocktail_cleaned[cocktail_uniques_elements.columns]

    return [cocktail_cleaned,cocktail_filters,cocktail_uniques_elements,cocktail_element_pertinent]

def initialisationBeer():

    ##
    beers_cleaned = pandas.read_csv('dataBases/Samples/beer_samples.csv')
    beers_elements_pertinent = ['Unnamed: 0','Name','brewery_name','beer_style']
    beers_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/beers_unique_elements.csv')
    beers_filters = beers_cleaned[beers_uniques_elements.columns]

    return [beers_cleaned,beers_filters,beers_uniques_elements,beers_elements_pertinent]

def initialisationMocktail():

    ##
    mocktail_cleaned = pandas.read_csv('dataBases/Samples/mocktail_samples.csv')
    mocktail_elements_pertinents = ['Unnamed: 0','Name','User Rating']
    mocktail_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/mocktail_unique_elements.csv')
    mocktail_filters = mocktail_cleaned[mocktail_uniques_elements.columns]
    
    return [mocktail_cleaned,mocktail_filters,mocktail_uniques_elements,mocktail_elements_pertinents]

def initilisationSoft():
    db_wine = initialisationWine()
    db_coffee = initilisationCoffee()
    db_cocktail = initilisationCocktail()
    db_beer = initialisationBeer()
    db_mocktail = initialisationMocktail()
    return [db_wine,db_cocktail,db_beer,db_coffee,db_mocktail]


dbsall = initilisationSoft()
dbs = dbsall[0]


def choisir_db(index,index_col):
    return dbsall[index][index_col]