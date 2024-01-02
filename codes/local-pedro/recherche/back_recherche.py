import pandas as pd
import csv 


#Filtre les databases sur une colone donée avec un filtre précis
def filtrer(f,colonne,data_Frame):
    return data_Frame[data_Frame[colonne] == f]

#Retourne les noms des colonnes de la bdd chargée ainsi que les types des colonnes (utile pour les comparaisons)
def colonnes(data_Frame):
    columns = data_Frame.columns
    types = data_Frame.dtypes
    L = []
    for i in range(len(colonnes)):
        L.append([columns[i],types[i]])
    return L
