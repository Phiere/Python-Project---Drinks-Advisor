import pandas
import csv

################################################################
################################################################
################################################################
#Fichier où on va créer les samples et extraire les éléments uniques 
#pour faire de l'autocomplétion sur les filtres 
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

nbIng = 1

brewery = beers['brewery_name']
brewery = brewery.drop_duplicates()


#####
#Style
#####

style = beers["beer_style"]
style = style.drop_duplicates()

#####
#Nom
#####

name = beers["beer_name"]
name = name.drop_duplicates()

#####
#ABV
#####

abv = beers["beer_abv"]
abv = abv.drop_duplicates()

#####
#Note overall
#####

note_overall = beers["review_overall"]
note_overall = note_overall.drop_duplicates()

#####
#Note arôme
#####

note_arome = beers["review_aroma"]
note_arome = note_arome.drop_duplicates()

#####
#Note apparence
#####

note_apparence = beers["review_appearance"]
note_apparence = note_apparence.drop_duplicates()

#####
#Note palate
#####

note_palate = beers["review_palate"]
note_palate= note_palate.drop_duplicates()

#####
#Note goût
#####

note_taste = beers["review_taste"]
note_taste= note_palate.drop_duplicates()



################################################################
#Création de la df
################################################################

data = {
    'Brasserie' : brewery,
    'Style' : style,
    'Nom': name,
    'Note Overall': note_overall,
    'Note Arome': note_arome,
    'Note Apparence': note_apparence,
    'Note Palate': note_palate,
    'Note Gout': note_taste,
}

Uniques_elements = pandas.DataFrame(data)
Uniques_elements.to_csv("/Users/pierrehelas/Documents/IOGS/3A/Code/Python-Project---Drinks-Advisor/dataBases/Filtering/beers_unique_elements.csv")
