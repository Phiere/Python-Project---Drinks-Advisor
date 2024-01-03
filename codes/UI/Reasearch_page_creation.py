import pandas as pd
import csv
import sys
import typing
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureWidget
import matplotlib.pyplot as plt
import back_recherche as br 
import Autocompletion


vins_complet = pd.read_csv('dataBases/Samples/wine_review_samples.csv')
vins_details = vins_complet[['country','designation','points','province']]

###Ok c'est bien mais je peux pas lier de méthode, c'est dommage ça fait des répétitions. Peut être faire une plus grosse classe gloabel et du fais le layout àc oter

#### la bouton random n'a pas été activé

### Je fais souvent appel à columns sans back_recherche. Peut etre faudrait stocker les colonne quelques parts ?

##BUENO
class Filtre(QWidget):
    def __init__(self,name_column,displayed_text) -> None:
        super().__init__()
        self.nom_col = name_column

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText(displayed_text)

##Servira de classe mère pour les retours menus, home profil. Pour l'instant c'est juste du layout
class MenuLayout(QWidget): 
    def __init__(self) -> None:
        super().__init__()
        self.menuLayout = QHBoxLayout()
        boutonAcceuil = QPushButton('Home')
        boutonRetour = QPushButton('Back')
        boutonSettings = QPushButton('Settings')
        self.menuLayout.addWidget(boutonAcceuil)
        self.menuLayout.addWidget(boutonRetour, alignment=Qt.AlignLeft)
        self.menuLayout.addWidget(boutonSettings)

##Creer une combobox sur le nombre d'éléments à afficher dans la la liste filtrée
class ComboBoxNbElements(QWidget):
    def __init__(self):
        super().__init__()

        self.comboBox = QComboBox()

        # Ajouter des options à la liste déroulante
        self.comboBox.addItem('10')
        self.comboBox.addItem('20')
        self.comboBox.addItem('50')
        self.comboBox.addItem('All')


        # Layout vertical
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.comboBox)

##Creer une combobox sur le noms de la colonne sur laquelle le tri d'affichage sera fait 
class ComboBoxColumnNames(QWidget):
    def __init__(self,L) -> None:
        super().__init__()

        self.comboBox = QComboBox()

        # Ajouter des options à la liste déroulante
        for text in L :
            print(text)
            self.comboBox.addItem(text)

        # Layout vertical
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.comboBox)

##Barre d'options pour gérer l'affichage de la liste filtrée
class FilterOptionsBar(QWidget):
    def __init__(self,data_frame) -> None:
        super().__init__()

        self.listoption = QHBoxLayout()
        self.rdchoice = QPushButton("random")
        self.ascchoice = ComboBoxColumnNames(data_frame.columns)
        self.ascgo = QPushButton('dsc')
        self.nbchoix = ComboBoxNbElements()
        self.listoption.addWidget(self.rdchoice)
        self.listoption.addLayout(self.nbchoix.layout)
        self.listoption.addLayout(self.ascchoice.layout)
        self.listoption.addWidget(self.ascgo)

##Creer l'affichage de tous les éléments trier comme des texte_edits. CLairement c'est le points à modifier les
##text edit vont pas du tout.
        
class CustomListAffichageTri(QWidget):
    def __init__(self,textearemplir):
        super().__init__()
        layout = QHBoxLayout(self)
        ## Créer des zones de textes pour chaque éléments (temporaire, faudra faire plus beau la c'est des texte basiques)
        self.lineEdits = [QLineEdit(self) for _ in range(len(textearemplir))]
        for i in range(len(self.lineEdits)):
            lineEdit = self.lineEdits[i]
            lineEdit.setText(textearemplir[i])
            layout.addWidget(lineEdit)

##Creation de l'écran
class ScreenResearch(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Description Window")
        self.resize(900,500)

        ##Cette info viendra de la page d'acceuil
        self.data_frame = vins_complet

        #Création des layouts généraux
        menuLayout = MenuLayout()
        descriptionLayout = QHBoxLayout()
        self.filtresLayout = QVBoxLayout()
        self.screenLayout = QVBoxLayout()
        
        #Ajout des filtres dynamiques
        self.L = self.creationFiltre(self.data_frame)
        for i in range(len(self.L)):
            self.filtresLayout.addWidget(self.L[i].name_edit)

        #Ajout de la barre d'option des filtres
        self.optionsdefiltres = FilterOptionsBar(self.data_frame)
        self.optionsdefiltres.nbchoix.comboBox.activated[str].connect(self.taketext)
        self.optionsdefiltres.ascchoice.comboBox.activated[str].connect(self.taketext)
        self.optionsdefiltres.ascgo.clicked.connect(self.changersens)
        self.etat = True

        #Complétion des layout
        self.listlayout = QVBoxLayout()
        self.listWidget = QListWidget()
        self.listlayout.addLayout(self.optionsdefiltres.listoption)
        self.listlayout.addWidget(self.listWidget)
        self.listWidget.setMinimumSize(QSize(600,500))

        #remplissage aléaotire pour un premier affichage
        self.changer_text(self.data_frame)

        #Assemblage layout
        descriptionLayout.addLayout(self.listlayout)
        descriptionLayout.addLayout(self.filtresLayout)
        self.screenLayout.addLayout(menuLayout.menuLayout)
        self.screenLayout.addLayout(descriptionLayout)
        self.setLayout(self.screenLayout)
        
    
    ##On créer les filtres dynamiquements selon les catégories de la bdd choisie
    def creationFiltre(self,df_p):
        colonnes = df_p.columns
        L = []
        for i in range(len(colonnes)):
            filtre = Filtre(colonnes[i],colonnes[i])
            L.append(filtre)
        for i in range(len(L)):
            L[i].name_edit.textEdited.connect(self.taketext)

        return L
    
    def taketext(self):
        Liste = self.L
        G = []
        for i in range(len(Liste)):
            G.append( Liste[i].name_edit.text())
        self.chargerNewDf(G)


    def chargerNewDf(self,G):
        tempdf = self.data_frame.copy()
        for i in range(len(G)) :
            if G[i] != '':
                nedt = self.L[i]
                if tempdf.dtypes[i] == type(1) :
                    tempdf = br.filtrer(int(G[i]),self.L[i].nom_col,tempdf)
                else :
                    tempdf = br.filtrer(G[i],self.L[i].nom_col,tempdf)
            print(tempdf)


        colonne = self.optionsdefiltres.ascchoice.comboBox.currentText()
        tempdf = tempdf.sort_values(colonne,ascending=self.etat)
        self.changer_text(tempdf)

    ##Pour choisir si l'affichage se fera en croissant ou décroissant
    def changersens(self):
        texte  = self.optionsdefiltres.ascgo.text()

        if texte == "dsc" :
            self.optionsdefiltres.ascgo.setText('asc')
            print("oui")
        else :
            self.optionsdefiltres.ascgo.setText('dsc')

        self.etat = not(self.etat)
        self.taketext()
    
    ##Gere l'affichage en fonction de tous les éléments choisis
    def changer_text(self,newdf):
        #choix du nombre d'éléments
        choix = self.optionsdefiltres.nbchoix.comboBox.currentText()
        n=0
        if choix == 'All' :
            n = len(newdf)
        else :
            n = int(self.optionsdefiltres.nbchoix.comboBox.currentText()) 

        if not(newdf.empty) and len(newdf) > n:
            self.listWidget.clear()

            for i in range(n):# Exemple avec 10 éléments
                listItem = QListWidgetItem(self.listWidget)
                texte = [str(newdf.iat[i,j]) for j in range(2,len(newdf.columns))]
                customItemWidget = CustomListAffichageTri(textearemplir=texte)
                listItem.setSizeHint(customItemWidget.sizeHint())
                self.listWidget.addItem(listItem)
                self.listWidget.setItemWidget(listItem, customItemWidget)
            #self.listlayout.updae()
     
        
        elif not(newdf.empty) :

            self.listWidget.clear()

            for i in range(len(newdf)):  
                listItem = QListWidgetItem(self.listWidget)
                texte = [str(newdf.iat[i,j]) for j in range(2,len(newdf.columns))]
                customItemWidget = CustomListAffichageTri(textearemplir=texte)
                listItem.setSizeHint(customItemWidget.sizeHint())
                self.listWidget.addItem(listItem)
                self.listWidget.setItemWidget(listItem, customItemWidget)
        
        


    
 
### C'est bien, peut être ajouter un bouton "rechercher" pour forcer la recherche et du coup montrer que ya pas
        
            

def main():
    app = QApplication(sys.argv)
    fenetre = ScreenResearch()
    fenetre.show()
    app.exec()



if __name__ == '__main__':
    main()
    
