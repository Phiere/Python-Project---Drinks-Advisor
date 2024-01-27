import pandas
import sys
sys.path.append('codes/UI/Screens/')


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


    wines_titles = ['winery','Name','price']
    wines_descriptions = ['Name','description','ponts','price','province','variety','winery','region_']
    wines_filtrage = ['country','Name','points','variety','winery','price','province','region_']
    wines_sort = ['Name','points','price','PersonalRating']

    wines_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/wines_unique_elements.csv')
    wines_filters = wines_uniques_elements[wines_filtrage]

    return [wines_cleaned,wines_filters,wines_titles,wines_descriptions,wines_sort]

def initilisationCoffee():

    ##
    coffee_cleaned = pandas.read_csv('dataBases/Samples/coffee_samples.csv')

    coffees_titles = ['Name','rating','loc_country','100g_USD']
    coffees_descriptions = ['Name','roaster','roast','loc_country','100g_USD','rating','origin_','desc_']
    coffees_filtrage =  ['roaster','roast','loc_country','100g_USD','rating','origin_']
    coffees_sort = ['Name','100g_USD','rating','PersonalRating']

    coffee_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/coffee_unique_elements.csv')
    coffee_filters = coffee_uniques_elements[coffees_filtrage]

    return [coffee_cleaned,coffee_filters,coffees_titles,coffees_descriptions,coffees_sort]

def initilisationCocktail():

    ##
    cocktail_cleaned = pandas.read_csv('dataBases/Samples/cocktails_samples.csv')
    
    cocktails_titles = ['Name','strAlcoholic','strIBA']
    cocktails_descriptions = ['Name','strAlcoholic','strCategory','strGlass','strIBA','strInstructions','strIngredient','strMeasure']
    cocktails_filtrage = ['strAlcoholic','strCategory','strGlass','strIBA','strIngredient']
    cocktails_sort = ['Name','PersonalRating']

    cocktail_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/cocktail_unique_elements.csv')
    cocktail_filters = cocktail_uniques_elements[cocktails_filtrage]

    return [cocktail_cleaned,cocktail_filters,cocktails_titles,cocktails_descriptions,cocktails_sort]

def initialisationBeer():

    ##
    beers_cleaned = pandas.read_csv('dataBases/Samples/beer_samples.csv')

    beers_titles = ['Name','beer_style','review_overall']
    beers_descriptions = ['brewery_name','beer_style','Name','review_overall','review_aroma','review_appearance','review_palate','review_taste','beer_abv' ]
    beers_filtrage = ['brewery_name','beer_style','review_overall','review_aroma','review_appearance','review_palate','review_taste','beer_abv' ]
    beers_sort = ['PersonalRating']

    beers_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/beers_unique_elements.csv')
    beers_filters = beers_uniques_elements[beers_filtrage]

    return [beers_cleaned,beers_filters,beers_titles,beers_descriptions,beers_sort]

def initialisationMocktail():

    ##
    mocktail_cleaned = pandas.read_csv('dataBases/Samples/mocktail_samples.csv')

    mocktails_titles = ['Name','Flavor Profile ','User Rating']
    mocktails_description = ['Name','User Rating','Ingredient ','Flavor Profile ']
    mocktails_filtrage = ['User Rating','Ingredient ','Flavor Profile ']
    mocktail_sort = ['User Rating','PersonalRating']

    mocktail_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/mocktail_unique_elements.csv')
    mocktail_filters = mocktail_uniques_elements[mocktails_filtrage]
    
    return [mocktail_cleaned,mocktail_filters,mocktails_titles,mocktails_description,mocktail_sort]

def initilisationSoft():
    db_wine = initialisationWine()
    db_coffee = initilisationCoffee()
    db_cocktail = initilisationCocktail()
    db_beer = initialisationBeer()
    db_mocktail = initialisationMocktail()
    return [db_wine,db_cocktail,db_beer,db_coffee,db_mocktail]


dbsall = initilisationSoft()

#Données globales pour l'application
dbs = dbsall[0]
choix_de_la_data_base = 0
index_boisson = 0