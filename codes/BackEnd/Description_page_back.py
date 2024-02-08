import Db_gestions as Db
import pandas as pd


def get_name_from_drink():
    db,index = Db.choix_de_la_data_base,Db.index_boisson
    boisson = Db.dbsall[db][0].iloc[index]
    name = boisson['Name']
    return name 

def get_description_from_drink():
    db,index = Db.choix_de_la_data_base,Db.index_boisson
    boisson = Db.dbsall[db][0].iloc[index]
    columns_to_read = Db.dbsall[db][3]
    text = ""
    skip_next_iterations = False

    for colonne in columns_to_read :
        if skip_next_iterations:
            break 

        value = boisson[colonne]

        if isinstance(value, list):
            value_str = ', '.join(str(item) for item in value)
        elif colonne == 'Price' and str(value) != 'Unfilled':
            if Db.choix_de_la_data_base == 0 : 
                value_str = f"{value} $"
            elif Db.choix_de_la_data_base == 3: 
                value_str = f"{value} $/100g"
        elif colonne == 'ReviewsNumber':
            value_str = f"{int(boisson[colonne]):,}"
        elif value not in ['',' ', 'nan']:
            value_str = str(value)

        if value_str.startswith('[') and value_str.endswith(']'):
            value_list = [item.strip("' ") for item in value_str[1:-1].split(',')]
            seen_elements = set()
            value_list_filtered = [item for item in value_list if item != 'nan' and item != '' and item != ' ' and (item not in seen_elements and seen_elements.add(item) is None)]
            value_str = ', '.join(value_list_filtered)
        
        text += str(colonne) + ' : ' + value_str + '\n' + '\n'

        if Db.choix_de_la_data_base == 2 and colonne == 'ReviewsNumber':
            text += "Rating (/5) : \n"
            index_OverallReview = columns_to_read.index('ReviewsNumber')
            for colonne in columns_to_read[index_OverallReview+1:]:
                text += '\n' + f"   - {str(colonne)} : {int(boisson[colonne]):,}" + '\n'
            skip_next_iterations = True            
    return text
        
def get_status_favori():
    db,index =  Db.choix_de_la_data_base,Db.index_boisson
    favory = Db.dbsall[db][0].at[index,'Favorite']
    return favory

def update_status_favori():
    db,index =  Db.choix_de_la_data_base, Db.index_boisson
    favory = not(Db.dbsall[db][0].iloc[index][-1])
    Db.dbsall[db][0].at[index,'Favorite'] = favory
    return favory

def get_comment():
    db,index =  Db.choix_de_la_data_base, Db.index_boisson
    comment = Db.dbsall[db][0].at[index,'Comment']
    if pd.isna(comment): return 'Leave a comment on the drink...'
    return comment

def update_comment(commentary):
    db,index =  Db.choix_de_la_data_base, Db.index_boisson
    Db.dbsall[db][0].at[index,'Comment'] = commentary

def get_rating():
    db,index = Db.choix_de_la_data_base,  Db.index_boisson
    rating = Db.dbsall[db][0].at[index,'PersonalRating']
    return rating

def update_rating(rating):
    db,index =  Db.choix_de_la_data_base,Db.index_boisson
    Db.dbsall[db][0].at[index,'PersonalRating'] = rating
