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

    #Changements des noms de colonnes
    wines_cleaned2 = wines_cleaned.copy()
    new_column_names = {'country' : 'Country', 'description' : 'Description', 'points' : 'Points', 
                        'price' : 'Price', 'province' : 'Province', 'variety' : 'Variety', 'winery' : 'Winery', 
                        'region_' : 'Region', 'Commentary' : 'Comment', 'Favories' : 'Favorite'}
    wines_cleaned2 = wines_cleaned2.rename(columns=new_column_names)
    #Enregistrement du fichier
    nom_fichier_csv = 'dataBases/samples/wines_samples2.csv'
    wines_cleaned2.to_csv(nom_fichier_csv, index=True)

    # Filtrage
    wines_titles = ['Name', 'Country', 'Winery', 'Price']
    wines_descriptions = ['Country','Winery','Province','Region','Variety','Points','Price','Description']
    wines_filtrage = ['Name', 'Country', 'Winery', 'Variety', 'Province', 'Region', 'Points','Price',]
    wines_sort = ['Name', 'Country', 'Variety', 'Points','Price','PersonalRating']

    wines_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/wines_unique_elements.csv')
    #Changements des noms de colonnes
    wines_uniques_elements2 = wines_uniques_elements.copy()
    wines_uniques_elements2 = wines_uniques_elements2.rename(columns=new_column_names)
    #Enregistrement du fichier
    nom_fichier_csv = 'dataBases/Filtering/Uniques_elements/wines_unique_elements2.csv'
    wines_uniques_elements2.to_csv(nom_fichier_csv, index=True)

    # Filtrage
    wines_filters = wines_uniques_elements2[wines_filtrage]
    wines_cleaned2.fillna("Unfilled", inplace=True)

    return [wines_cleaned2,wines_filters,wines_titles,wines_descriptions,wines_sort]

def initilisationCoffee():

    ##
    coffee_cleaned = pandas.read_csv('dataBases/Samples/coffee_samples.csv', index_col=0)
    #Changements des noms de colonnes
    coffee_cleaned2 = coffee_cleaned.copy()
    new_column_names = {'roaster' : 'Roaster', 'roast' : 'Roast', 'loc_country' : 'Country', 
                        '100g_USD' : 'Price', 'rating' : 'UserRating', 'review_date' : 'ReviewDate', 'origin_' : 'Origin', 
                        'desc_' : 'Description', 'Commentary' : 'Comment', 'Favories' : 'Favorite'}
    coffee_cleaned2 = coffee_cleaned2.rename(columns=new_column_names)
    #Enregistrement du fichier
    nom_fichier_csv = 'dataBases/samples/coffee_samples2.csv'
    coffee_cleaned2.to_csv(nom_fichier_csv, index=True)

    #Filtrage
    coffees_titles = ['Name', 'Country', 'Roaster','Price']
    coffees_descriptions = ['Country','Roaster','Roast','Origin','Price','Description','UserRating']
    coffees_filtrage =  ['Name','Country','Roaster','Roast','Origin','Price','UserRating']
    coffees_sort = ['Name','Country','Roaster','Roast','Price','UserRating','PersonalRating']

    coffee_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/coffee_unique_elements.csv')
    #Changements des noms de colonnes
    coffee_uniques_elements2 = coffee_uniques_elements.copy()
    coffee_uniques_elements2 = coffee_uniques_elements2.rename(columns=new_column_names)
    #Enregistrement du fichier
    nom_fichier_csv = 'dataBases/Filtering/Uniques_elements/coffee_uniques_elements2.csv'
    coffee_uniques_elements2.to_csv(nom_fichier_csv, index=True)

    #Filtrage
    coffee_filters = coffee_uniques_elements2[coffees_filtrage]
    coffee_cleaned.fillna("Unfilled", inplace=True)

    return [coffee_cleaned2,coffee_filters,coffees_titles,coffees_descriptions,coffees_sort]

def initilisationCocktail():

    ##
    cocktail_cleaned = pandas.read_csv('dataBases/Samples/cocktails_samples.csv', index_col=0)
    #Changements des noms de colonnes
    cocktail_cleaned2 = cocktail_cleaned.copy()
    new_column_names = {'dateModified' : 'ModificationDate', 'idDrink' : 'DrinkID', 'strAlcoholic' : 'DrinkType', 
                        'strCategory' : 'Category', 'strDrinkThumb' : 'GlassImageLink', 'strGlass' : 'Glass', 'strIBA' : 'IBA', 'strInstructions' : 'Recipe', 
                        'strVideo' : 'Video', 'strIngredient' : 'Ingredients', 'strMeasure' : 'Measure', 'Commentary' : 'Comment', 'Favories' : 'Favorite'}
    cocktail_cleaned2 = cocktail_cleaned2.rename(columns=new_column_names)
    #Enregistrement du fichier
    nom_fichier_csv = 'dataBases/samples/cocktail_samples2.csv'
    cocktail_cleaned2.to_csv(nom_fichier_csv, index=True)

    #Filtrage
    cocktails_titles = ['Name','DrinkType','Category']
    cocktails_descriptions = ['DrinkType','Category','Glass','GlassImageLink','Ingredients','Measure','Recipe']
    cocktails_filtrage = ['Name','DrinkType','Category','Glass','Ingredients']
    cocktails_sort = ['Name','DrinkType','Category','PersonalRating']

    cocktail_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/cocktail_unique_elements.csv')
    #Changements des noms de colonnes
    cocktail_uniques_elements2 = cocktail_uniques_elements.copy()
    cocktail_uniques_elements2 = cocktail_uniques_elements2.rename(columns=new_column_names)
    #Enregistrement du fichier
    nom_fichier_csv = 'dataBases/Filtering/Uniques_elements/cocktail_uniques_elements2.csv'
    cocktail_uniques_elements2.to_csv(nom_fichier_csv, index=True)

    #Filtrage
    cocktail_filters = cocktail_uniques_elements2[cocktails_filtrage]
    cocktail_cleaned.fillna("Unfilled", inplace=True)

    return [cocktail_cleaned2,cocktail_filters,cocktails_titles,cocktails_descriptions,cocktails_sort]

def initialisationBeer():

    ##
    beers_cleaned = pandas.read_csv('dataBases/Samples/beer_samples.csv', index_col=0)
    #Changements des noms de colonnes
    beers_cleaned2 = beers_cleaned.copy()
    new_column_names = {'brewery_name' : 'Brewery', 'beer_style' : 'Style', 'beer_beerid' : 'BeerID', 
                        'brewery_id' : 'BreweryID', 'review_time' : 'ReviewsNumber', 'review_overall' : 'OverallReview',
                        'review_aroma' : 'Aroma', 'review_appearance' : 'Appearance', 'review_palate' : 'Palate', 'review_taste' : 'Taste', 
                        'beer_abv' : 'BeerABV','Commentary' : 'Comment', 'Favories' : 'Favorite'}
    beers_cleaned2 = beers_cleaned2.rename(columns=new_column_names)
    #Enregistrement du fichier
    nom_fichier_csv = 'dataBases/samples/beers_samples2.csv'
    beers_cleaned2.to_csv(nom_fichier_csv, index=True)

    #Filtrage
    beers_titles = ['Name','Style','Brewery','OverallReview']
    beers_descriptions = ['Brewery','Style','OverallReview','ReviewsNumber','Aroma','Appearance','Palate','Taste']
    beers_filtrage = ['Name','Style','Brewery','OverallReview','Aroma','Appearance','Palate','Taste','ReviewsNumber']
    beers_sort = ['Name','Style','Brewery','OverallReview','Aroma','Appearance','Palate','Taste','PersonalRating']

    beers_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/beers_unique_elements.csv')
    #Changements des noms de colonnes
    beers_uniques_elements2 = beers_uniques_elements.copy()
    beers_uniques_elements2 = beers_uniques_elements2.rename(columns=new_column_names)
    #Enregistrement du fichier
    nom_fichier_csv = 'dataBases/Filtering/Uniques_elements/beers_uniques_elements2.csv'
    beers_uniques_elements2.to_csv(nom_fichier_csv, index=True)

    #Filtrage
    beers_filters = beers_uniques_elements2[beers_filtrage]

    beers_cleaned.fillna("Unfilled", inplace=True)

    return [beers_cleaned2,beers_filters,beers_titles,beers_descriptions,beers_sort]

def initialisationMocktail():

    ##
    mocktail_cleaned = pandas.read_csv('dataBases/Samples/mocktail_samples.csv', index_col=0)
    #Changements des noms de colonnes
    mocktail_cleaned2 = mocktail_cleaned.copy()
    new_column_names = {'User Rating' : 'UserRating', 'Ingredient ' : 'Ingredients', 'Flavor Profile ' : 'FlavorProfile', 
                        'Commentary' : 'Comment', 'Favories' : 'Favorite'}
    mocktail_cleaned2 = mocktail_cleaned2.rename(columns=new_column_names)
    #Enregistrement du fichier
    nom_fichier_csv = 'dataBases/samples/mocktail_samples2.csv'
    mocktail_cleaned2.to_csv(nom_fichier_csv, index=True)

    #Filtrage
    mocktails_titles = ['Name','FlavorProfile','UserRating']
    mocktails_description = ['Ingredients','FlavorProfile','UserRating']
    mocktails_filtrage = ['Name','FlavorProfile','Ingredients','UserRating']
    mocktail_sort = ['Name','UserRating','PersonalRating']

    mocktail_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/mocktail_unique_elements.csv')
    #Changements des noms de colonnes
    mocktail_uniques_elements2 = mocktail_uniques_elements.copy()
    mocktail_uniques_elements2 = mocktail_uniques_elements2.rename(columns=new_column_names)
    #Enregistrement du fichier
    nom_fichier_csv = 'dataBases/Filtering/Uniques_elements/mocktail_uniques_elements2.csv'
    mocktail_uniques_elements2.to_csv(nom_fichier_csv, index=True)

    #Filtrage
    mocktail_filters = mocktail_uniques_elements2[mocktails_filtrage]

    mocktail_cleaned.fillna("Unfilled", inplace=True)
    
    return [mocktail_cleaned2,mocktail_filters,mocktails_titles,mocktails_description,mocktail_sort]

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