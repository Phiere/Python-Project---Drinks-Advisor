from Importations import *
import Research_page_creation_back as Rb

#### la bouton random n'a pas été activé
### peut être ajouter un bouton "rechercher" pour forcer la recherche et du coup montrer que ya pas
### Comment faire avec les listes ? Pour l'instant ça ne fonctionne pas

dbs = DB.choix_db('Cocktail')
print(dbs[2])

"""Wines = pandas.read_csv('dataBases/Samples/wine_review_samples.csv')
Wines_filters = Wines[['country','designation','points','price']]
Wines_uniques_elements = pandas.read_csv('dataBases/Filtering/Uniques_elements/wines_unique_elements.csv')
dbs = [Wines,Wines_filters,Wines_uniques_elements]"""

#Les filtres sont des éléments qui dependent de la database choisi et des éléments pertinents.
#C'est eux qui, si on les remplis, peuvent trier les résultats affichés
class Filtre(QWidget):
    def __init__(self,name_column,displayed_text) -> None:
        super().__init__()
        self.nom_col = name_column

        self.name_edit_list = []
        self.nb_elements = 1
        if "list" in name_column:
            self.nb_elements = int(name_column[-1])
            if name_column[-2] == '1' :
                self.nb_elements += int(name_column[-2])*10
            for i in range(self.nb_elements):
                autocompleter = Rb.from_name_to_unique_elements_completer(name_column)
                name_edit = autocompleter.lineEdit
                name_edit.setPlaceholderText(displayed_text)
                self.name_edit_list.append(name_edit)
                
        else :
            autocompleter = Rb.from_name_to_unique_elements_completer(name_column)
            name_edit = autocompleter.lineEdit
            name_edit.setPlaceholderText(displayed_text)
            self.name_edit_list.append(name_edit)
       

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
    def __init__(self,columns_names_list) -> None:
        super().__init__()

        self.comboBox = QComboBox()

        # Ajouter des options à la liste déroulante
        for text in columns_names_list:
            print(text)
            self.comboBox.addItem(text)

        # Layout vertical
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.comboBox)

##Barre d'options pour gérer l'affichage de la liste filtrée
class FilterOptionsBar(QWidget):
    def __init__(self,ecran,data_frame) -> None:
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

        self.nbchoix.comboBox.activated[str].connect(ecran.chargerNewDf)
        self.ascchoice.comboBox.activated[str].connect(ecran.chargerNewDf)
        self.ascgo.clicked.connect(ecran.changersens)


##Creer l'affichage de tous les éléments trier comme des texte_edits. CLairement c'est le points à modifier les
##text edit vont pas du tout.
        
class CustomListAffichageTri(QWidget):
    def __init__(self,completion_text_to_display):
        super().__init__()
        layout = QHBoxLayout(self)
        ## Créer des zones de textes pour chaque éléments (temporaire, faudra faire plus beau la c'est des texte basiques)
        self.lineEdits = [QLineEdit(self) for _ in range(len(completion_text_to_display))]
        for i in range(len(self.lineEdits)):
            lineEdit = self.lineEdits[i]
            lineEdit.setText(completion_text_to_display[i])
            layout.addWidget(lineEdit)

##Creation de l'écran
class ScreenResearch(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Description Window")
        self.resize(1000,500)

        ##Cette info viendra de la page d'acceuil
        self.data_frame = dbs[1]

        #Création des layouts généraux
        menuLayout = MenuLayout()
        descriptionLayout = QHBoxLayout()
        self.filtresLayout = QVBoxLayout()
        self.screenLayout = QVBoxLayout()
        
        #Ajout des filtres dynamiques
        self.filters_list = self.creationFiltre(self.data_frame)
        for i in range(len(self.filters_list)):
            for j in range(self.filters_list[i].nb_elements):
                self.filtresLayout.addWidget(self.filters_list[i].name_edit_list[j])

        #self.filtresLayout.setMinimumWidth(200)
        self.filtresLayout.minimumSize()
        
        self.optionsdefiltres = FilterOptionsBar(self,self.data_frame,)
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
        descriptionLayout.addLayout(self.listlayout,8)
        descriptionLayout.addLayout(self.filtresLayout,2)
        self.screenLayout.addLayout(menuLayout.menuLayout)
        self.screenLayout.addLayout(descriptionLayout)
        self.setLayout(self.screenLayout)
        
    
    ##On créer les filtres dynamiquements selon les catégories de la bdd choisie
    def creationFiltre(self,df_p):
        return Rb.from_df_to_filters(df_p,self.chargerNewDf)

    #Charher la df filtrée avec les filtres
    def chargerNewDf(self):
        tempdf = Rb.from_filters_to_newDF(self.data_frame,self.filters_list,self.optionsdefiltres.ascchoice.comboBox.currentText(),self.etat)
        self.changer_text(tempdf)


    ##Pour choisir si l'affichage se fera en croissant ou décroissant
    def changersens(self):
        new_sorted_choice = Rb.chose_sorted_sens(self.optionsdefiltres.ascgo.text())
        self.optionsdefiltres.ascgo.setText(new_sorted_choice)
        self.etat=not(self.etat)
        self.chargerNewDf()

    
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
                texte = [str(newdf.iat[i,j]) for j in range(len(newdf.columns))]
                customItemWidget = CustomListAffichageTri(texte)
                listItem.setSizeHint(customItemWidget.sizeHint())
                self.listWidget.addItem(listItem)
                self.listWidget.setItemWidget(listItem, customItemWidget)
            #self.listlayout.updae()
     
        
        elif not(newdf.empty) :

            self.listWidget.clear()

            for i in range(len(newdf)):  
                listItem = QListWidgetItem(self.listWidget)
                texte = [str(newdf.iat[i,j]) for j in range(len(newdf.columns))]
                customItemWidget = CustomListAffichageTri(texte)
                listItem.setSizeHint(customItemWidget.sizeHint())
                self.listWidget.addItem(listItem)
                self.listWidget.setItemWidget(listItem, customItemWidget)
        
        
            
def main():
    app = QApplication(sys.argv)
    fenetre = ScreenResearch()
    fenetre.show()
    app.exec()



if __name__ == '__main__':
    main()
    
