####################################
####################################
#Ouverture des BDD et créations des données filtrées pour l'autocomplétion etc
#Structure des fonctions :
#  ..._cleaned : Databases nettoyées et sous forme de liste pour les colonnes doubles. Contiennent toutes les données
#  ..._pertinents_elements : Liste des colonnes qui serviront de filtres pour la recherche
#  ..._unique_elements : Database des éléments uniques de toutes les colonnes
#  ..._filters : Database des éléments uniques pour les filtres de l'autocomplétion
#  ..._sort : liste des colonnes sur lesquelles il est possible/intéressant de trier
####################################
####################################

import pandas
import sys
sys.path.append('codes/UI/Screens/')

#V0.1
def data_frames_reding(path_db_clean,path_unique_elements,filtrage,titles,descriptions,sort):
    """Prend tous les paramètres d'un data_frame décidé au préalable et donne une liste de dataframe utilisable par l'application
    
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
                              path_unique_elements='dataBases/Uniques_elements/wines_unique_elements.csv',
                              filtrage=['Name', 'Country', 'Winery', 'Variety', 'Province', 'Region', 'Points','Price'],
                              titles=['Name', 'Country', 'Winery', 'Price'],
                              descriptions=['Country','Winery','Province','Region','Variety','Points','Price','Description'],
                              sort=['Name', 'Country', 'Variety','Winery','Points','Price','PersonalRating']
                              )

coffees_df = data_frames_reding(path_db_clean='dataBases/Samples/coffee_samples.csv',
                                path_unique_elements='dataBases/Uniques_elements/coffee_unique_elements.csv',
                                filtrage=['Name','Country','Roaster','Roast','Origin','Price','UserRating'],
                                titles=['Name', 'Country', 'Roaster','Price'],
                                descriptions=['Country','Roaster','Roast','Origin','Price','Description','UserRating'],
                                sort=['Name','Country','Roaster','Roast','Price','UserRating','PersonalRating']
                                )
                             
cocktails_df = data_frames_reding(path_db_clean='dataBases/Samples/cocktails_samples.csv',
                                  path_unique_elements='dataBases/Uniques_elements/cocktail_unique_elements.csv',
                                  filtrage=['Name','DrinkType','Category','Glass','Ingredients'],
                                  titles=['Name','DrinkType','Category'],
                                  descriptions=['DrinkType','Category','Glass','Ingredients','Measure','Recipe'],
                                  sort=['Name','DrinkType','Category','PersonalRating'],
                                )

beers_df = data_frames_reding(path_db_clean='dataBases/Samples/beer_samples.csv',
                              path_unique_elements='dataBases/Uniques_elements/beers_unique_elements.csv',
                              filtrage=['Name','Style','Brewery','OverallReview','Aroma','Appearance','Palate','Taste','ReviewsNumber'],
                              titles=['Name','Style','Brewery','OverallReview'],
                              descriptions=['Brewery','Style','OverallReview','ReviewsNumber','Aroma','Appearance','Palate','Taste'],
                              sort=['Name','Style','Brewery','OverallReview','Aroma','Appearance','Palate','Taste','PersonalRating']
                              )

mocktails_df = data_frames_reding(path_db_clean='dataBases/Samples/mocktail_samples.csv',
                                  path_unique_elements='dataBases/Uniques_elements/mocktail_unique_elements.csv',
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
list_elements = ['Region','Ingredients']
dbs = dbsall[0]
choix_de_la_data_base = 0
index_boisson = 0

def changes_save():
    """Sauvegarde tous les changements effectués dans les data_base pour la prochaine fois"""

    save_path_samples = ['dataBases/Samples/wines_samples.csv',
                         'dataBases/Samples/cocktails_samples.csv',
                         'dataBases/Samples/beer_samples.csv',
                         'dataBases/Samples/coffee_samples.csv',
                         'dataBases/Samples/mocktail_samples.csv',
                 ]
    save_path_uniques = ['dataBases/Uniques_elements/wines_unique_elements.csv',
                         'dataBases/Uniques_elements/cocktail_unique_elements.csv',
                         'dataBases/Uniques_elements/beers_unique_elements.csv',
                         'dataBases/Uniques_elements/coffee_unique_elements.csv',
                         'dataBases/Uniques_elements/mocktail_unique_elements.csv',
                  ]
    print("Enregistrement en cours")
    for i in range(len(save_path_samples)):
        db_sample = dbsall[i][0]
        db_elements = dbsall[i][1]

        db_sample.to_csv(save_path_samples[i])
        db_elements.to_csv(save_path_uniques[i])
        print("Enregistrement effectué : ",i," /",len(save_path_samples))


