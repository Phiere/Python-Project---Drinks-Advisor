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
#  ..._filters : Datase des éléments uniques pour les filtres de l'autocomplétion
####################################
####################################

def initialisationWine():

    ## Appels des databases préalablement nettoyées
    wines_cleaned = pandas.read_csv('dataBases/Samples/wines_samples.csv', index_col=0)
    

    # Filtrage
    wines_titles = ['Name', 'Country', 'Winery', 'Price']
    wines_descriptions = ['Country','Winery','Province','Region','Variety','Points','Price','Description']
    wines_filtrage = ['Name', 'Country', 'Winery', 'Variety', 'Province', 'Region', 'Points','Price',]
    wines_sort = ['Name', 'Country', 'Variety', 'Points','Price','PersonalRating']

    wines_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/wines_unique_elements.csv')

    # Filtrage
    wines_filters = wines_uniques_elements[wines_filtrage]

    return [wines_cleaned,wines_filters,wines_titles,wines_descriptions,wines_sort]

def initilisationCoffee():

    ##
    coffee_cleaned = pandas.read_csv('dataBases/Samples/coffee_samples.csv', index_col=0)

    #Filtrage
    coffees_titles = ['Name', 'Country', 'Roaster','Price']
    coffees_descriptions = ['Country','Roaster','Roast','Origin','Price','Description','UserRating']
    coffees_filtrage =  ['Name','Country','Roaster','Roast','Origin','Price','UserRating']
    coffees_sort = ['Name','Country','Roaster','Roast','Price','UserRating','PersonalRating']

    coffee_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/coffee_unique_elements.csv')

    #Filtrage
    coffee_filters = coffee_uniques_elements[coffees_filtrage]
    coffee_cleaned.fillna("Unfilled", inplace=True)

    return [coffee_cleaned,coffee_filters,coffees_titles,coffees_descriptions,coffees_sort]

def initilisationCocktail():

    ##
    cocktail_cleaned = pandas.read_csv('dataBases/Samples/cocktails_samples.csv', index_col=0)

    #Filtrage
    cocktails_titles = ['Name','DrinkType','Category']
    cocktails_descriptions = ['DrinkType','Category','Glass','GlassImageLink','Ingredients','Measure','Recipe']
    cocktails_filtrage = ['Name','DrinkType','Category','Glass','Ingredients']
    cocktails_sort = ['Name','DrinkType','Category','PersonalRating']

    cocktail_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/cocktail_unique_elements.csv')
 
    #Filtrage
    cocktail_filters = cocktail_uniques_elements[cocktails_filtrage]
    cocktail_cleaned.fillna("Unfilled", inplace=True)

    return [cocktail_cleaned,cocktail_filters,cocktails_titles,cocktails_descriptions,cocktails_sort]

def initialisationBeer():

    ##
    beers_cleaned = pandas.read_csv('dataBases/Samples/beer_samples.csv', index_col=0)

    #Filtrage
    beers_titles = ['Name','Style','Brewery','OverallReview']
    beers_descriptions = ['Brewery','Style','OverallReview','ReviewsNumber','Aroma','Appearance','Palate','Taste']
    beers_filtrage = ['Name','Style','Brewery','OverallReview','Aroma','Appearance','Palate','Taste','ReviewsNumber']
    beers_sort = ['Name','Style','Brewery','OverallReview','Aroma','Appearance','Palate','Taste','PersonalRating']

    beers_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/beers_unique_elements.csv')

    #Filtrage
    beers_filters = beers_uniques_elements[beers_filtrage]

    beers_cleaned.fillna("Unfilled", inplace=True)

    return [beers_cleaned,beers_filters,beers_titles,beers_descriptions,beers_sort]

def initialisationMocktail():

    ##
    mocktail_cleaned = pandas.read_csv('dataBases/Samples/mocktail_samples.csv', index_col=0)
    mocktail_cleaned.fillna("Unfilled", inplace=True)
    #Filtrage
    mocktails_titles = ['Name','FlavorProfile','UserRating']
    mocktails_description = ['Ingredients','FlavorProfile','UserRating']
    mocktails_filtrage = ['Name','FlavorProfile','Ingredients','UserRating']
    mocktail_sort = ['Name','UserRating','PersonalRating']

    mocktail_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/mocktail_unique_elements.csv')
    
    #Filtrage
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

categories = ['Wines', 'Cocktails', 'Beers', 'Coffees', 'Mocktails']

#Données globales pour l'application
dbs = dbsall[0]
choix_de_la_data_base = 0
index_boisson = 0