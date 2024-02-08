####################################
####################################
#Ouverture des BDD et créations des données filtrées pour l'autocomplétion etc
#Strcuture des fonctions :
#  ..._cleaned : Databases nettoyées et sous forme de liste pour les colonnes doubles. Contiennent toutes les données
#  ..._pertinents_elements : Liste des colonnes qui serviront de filtres pour la recherche
#  ..._unique_elements : Database des éléments uniques de toutes les colonnes
#  ..._filters : Datase des éléments uniques pour les filtres de l'autocomplétion
#  ..._sort : liste des colonnes sur lesquelle on va potentiellement vouloir trier
####################################
####################################

import pandas
import sys
sys.path.append('codes/UI/Screens/')

#V0.1
def data_frames_reding(path_db_clean,path_unique_elements,filtrage,titles,descriptions,sort):
    """Prend tous les paramètres d'un data_frame décidé au prélable et donne une liste de dataframe utilisable par l'application
    
    - path_db_clean : chemin vers la database de base
    - path_unique_elements : chemin vers la database des éléments uniques construite au préalable
    - filtrage : choix des colonnes qui serviront de filtres
    - titles : choix des colonnes à afficher dans la recherche
    - description : choix des colonnes à afficher dans la description
    - sort : choix des colonnes qui pourront servir de colonnes de tri dans l'affichage"""
    df_cleaned = pandas.read_csv(path_db_clean,index_col=0)
    df_uniques_element = pandas.read_csv(path_unique_elements,index_col=0)
    df_filters = df_uniques_element[filtrage]
    return [df_cleaned,df_filters,titles,descriptions,sort]


##Wines
wines_df = data_frames_reding(path_db_clean='dataBases/Samples/wines_samples.csv',
                              path_unique_elements='dataBases/Filtering/Uniques_elements/wines_unique_elements.csv',
                              filtrage=['Name', 'Country', 'Winery', 'Variety', 'Province', 'Region', 'Points','Price'],
                              titles=['Name', 'Country', 'Winery', 'Price'],
                              descriptions=['Country','Winery','Province','Region','Variety','Points','Price','Description'],
                              sort=['Name', 'Country', 'Variety', 'Points','Price','PersonalRating']
                              )

coffees_df = data_frames_reding(path_db_clean='dataBases/Samples/coffee_samples.csv',
                                path_unique_elements='dataBases/Filtering/Uniques_elements/coffee_unique_elements.csv',
                                filtrage=['Name','Country','Roaster','Roast','Origin','Price','UserRating'],
                                titles=['Name', 'Country', 'Roaster','Price'],
                                descriptions=['Country','Roaster','Roast','Origin','Price','Description','UserRating'],
                                sort=['Name','Country','Roaster','Roast','Price','UserRating','PersonalRating']
                                )
                             
cocktails_df = data_frames_reding(path_db_clean='dataBases/Samples/cocktails_samples.csv',
                                  path_unique_elements='dataBases/Filtering/Uniques_elements/cocktail_unique_elements.csv',
                                  filtrage=['Name','DrinkType','Category','Glass','Ingredients'],
                                  titles=['Name','DrinkType','Category'],
                                  descriptions=['DrinkType','Category','Glass','Ingredients','Measure','Recipe'],
                                  sort=['Name','DrinkType','Category','PersonalRating'],
                                )

beers_df = data_frames_reding(path_db_clean='dataBases/Samples/beer_samples.csv',
                              path_unique_elements='dataBases/Filtering/Uniques_elements/beers_unique_elements.csv',
                              filtrage=['Name','Style','Brewery','OverallReview','Aroma','Appearance','Palate','Taste','ReviewsNumber'],
                              titles=['Name','Style','Brewery','OverallReview'],
                              descriptions=['Brewery','Style','OverallReview','ReviewsNumber','Aroma','Appearance','Palate','Taste'],
                              sort=['Name','Style','Brewery','OverallReview','Aroma','Appearance','Palate','Taste','PersonalRating']
                              )

mocktails_df = data_frames_reding(path_db_clean='dataBases/Samples/mocktail_samples.csv',
                                  path_unique_elements='dataBases/Filtering/Uniques_elements/mocktail_unique_elements.csv',
                                  filtrage=['Name','FlavorProfile','Ingredients','UserRating'],
                                  titles=['Name','FlavorProfile','UserRating'],
                                  descriptions=['Ingredients','FlavorProfile','UserRating'],
                                  sort=['Name','UserRating','PersonalRating']
                                  )

#Données globales pour l'application
dbsall = [wines_df,cocktails_df,beers_df,coffees_df,mocktails_df]
categories = ['Wines', 'Cocktails', 'Beers', 'Coffees', 'Mocktails']
favories_titles = ['Type','Name','Personnal Rating']
number_elements = ['Price', 'Points', 'OverallReview','ReviewsNumber','Aroma','Appearance','Palate','Taste', 'UserRating']
dbs = dbsall[0]
choix_de_la_data_base = 0
index_boisson = 0


