import pandas
import csv

cocktail = pandas.read_csv("Raw_databases/all_drinks.csv")


cocktail_samples = cocktail.head(100)


def cocktail_write(L,data):
    for i in range(len(L)):
        if type(L[i]) != str:
            return Exception
        
    nouvelle_ligne = {'strDrink': [L[0]], 
                      'idDrink': [L[1]],
                      'strAlcoholic': [L[2]], 
                      'strCategory': [L[3]],
                      'strDrinkThumb': [L[4]], 
                      'strGlass': [L[5]],
                      'strIBA': [L[6]], 
                      'strIngredient1': [L[7]],
                      'strIngredient2': [L[8]],
                      'strIngredient3': [L[9]],
                      'strIngredient4': [L[10]],
                      'strIngredient5': [L[11]],
                      'strIngredient6': [L[12]],
                      'strIngredient7': [L[13]],
                      'strIngredient8': [L[14]],
                      'strIngredient9': [L[15]],
                      'strIngredient10': [L[16]],
                      'strIngredient11': [L[17]],
                      'strIngredient12': [L[18]],
                      'strIngredient13': [L[19]],
                      'strIngredient14': [L[20]],
                      'strIngredient15': [L[21]],
                      'strDrink': [L[22]], 
                      'idDrink': [L[23]],
                      'strInstructions': [L[24]], 
                      'strMesure1' : [L[25]],
                      'strMesure2' : [L[26]],
                      'strMesure3' : [L[27]],
                      'strMesure4' : [L[28]],
                      'strMesure5' : [L[29]],
                      'strMesure6' : [L[30]],
                      'strMesure7' : [L[31]],
                      'strMesure8' : [L[32]],
                      'strMesure9' :[ L[33]],
                      'strMesure10' : [L[34]],
                      'strMesure11' : [L[35]],
                      'strMesure12' : [L[36]],
                      'strMesure13' : [L[37]],
                      'strMesure14' : [L[38]],
                      'strMesure15' : [L[39]],
                      }

    nouvelle_ligne = pandas.DataFrame(nouvelle_ligne)
    print(nouvelle_ligne)
    data = pandas.concat([data,nouvelle_ligne])
    data.reset_index()
    data.to_csv('Samples/test_cocktail_recettes.csv', index=False)
    return 0


L = ['']*40
cocktail_write(L,cocktail_samples)

