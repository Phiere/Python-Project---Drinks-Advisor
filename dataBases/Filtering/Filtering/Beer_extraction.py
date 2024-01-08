import pandas
import csv

################################################################
################################################################
################################################################
#Fichier où on va créer les samples et extraire les éléments uniques 
#pour faire de l'autocomplétion sur les filtres. On va les créer comme une classes qui sera recréer à chaque lancement.
#Ainsi on prend en compte les modifications des recettes.

# Question : - On écrit les df avec les éléments uniques dans un fichier csv ?
# - On garde les élément uniques dans le cache ? (choix retenu pour l'instant)
################################################################
################################################################
################################################################

beers = pandas.read_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/PROTO PYTHON/Raw_databases/beer_reviews.csv")
#beers_samples = beers.head(100)
#beers_samples.to_csv("Samples/beers_samples.csv")

################################################################
#Extraction de chaque pays pour les bières :
################################################################

#####
#Brasserie
#####

brewery_name = beers['brewery_name']
brewery_name = brewery_name.drop_duplicates()

#####
#Style
#####

beer_style = beers["beer_style"]
beer_style = beer_style.drop_duplicates()

#####
#Nom
#####

beer_name = beers["beer_name"]
beer_name = beer_name.drop_duplicates()

#####
#ABV
#####

beer_abv = beers["beer_abv"]
beer_abv = beer_abv.drop_duplicates()

#####
#Note overall
#####

review_overall = beers["review_overall"]
review_overall = review_overall.drop_duplicates()

#####
#Note arôme
#####

review_aroma = beers["review_aroma"]
review_aroma = review_aroma.drop_duplicates()

#####
#Note apparence
#####

review_appearance = beers["review_appearance"]
review_appearance = review_appearance.drop_duplicates()

#####
#Note palate
#####

review_palate = beers["review_palate"]
review_palate= review_palate.drop_duplicates()

#####
#Note goût
#####

review_taste = beers["review_taste"]
review_taste= review_taste.drop_duplicates()

################################################################
#Création de la df
################################################################

data = {
    'brewery_name' : brewery_name,
    'beer_style' : beer_style,
    'beer_name': beer_name,
    'beer_abv' : beer_abv,
    'review_overall': review_overall,
    'review_aroma': review_aroma,
    'review_appearance': review_appearance,
    'review_palate': review_palate,
    'review_taste': review_taste,
}

Uniques_elements = pandas.DataFrame(data)
Uniques_elements.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/Uniques_elements/beers_unique_elements.csv")



