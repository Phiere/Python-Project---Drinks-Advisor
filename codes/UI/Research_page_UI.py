############################################################
############################################################
############################################################
#Contient le script pour constuire la page recherche, rassemblant les options de filtres, les options 
#de tris et les éléments filtrés.
############################################################
############################################################
############################################################

import sys
from PyQt5.QtGui import QIcon, QMouseEvent
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,QHBoxLayout,QPushButton,
                             QComboBox,QLabel,QListWidget,QListWidgetItem,QMessageBox)
from PyQt5.QtCore import Qt
sys.path.append('codes/BackEnd/')
import Db_gestions as Db
import Research_page_back as RB 


init = 0
############################################################
#Création des options de tri
############################################################
class NumberOfElementChoice(QComboBox):
    """Combo box permettant de choisir le nombre d'éléments à afficher.
    
    - upload_screen : fonction de refraîchissement de l'affichage en fonction du nombre d'éléments choisis
    """
    def __init__(self,upload_screen):
        super().__init__()
        self.setFixedSize(120, 40)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")

        # Ajouter des options arbitraires  à la liste déroulante
        self.addItem('10')
        self.addItem('20')
        self.addItem('50')
        self.addItem('100')
        self.activated[str].connect(upload_screen)


class SortColumnChoice(QComboBox):
    """Crée une combobox sur le nom de la colonne sur laquelle le tri d'affichage sera fait 
    
    - upload_screen : fonction de refraîchissement de l'affichage en fonction de la colonne de tri choisi
    - update : met à jour les possibilités de tri en fonction de la database choisie"""
    def __init__(self,upload_screen):
        super().__init__()
        self.activated[str].connect(upload_screen)
        self.setFixedSize(120,40)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")

        self.update()
       
    def update(self):
        names = Db.dbsall[Db.choix_de_la_data_base][4] 
        self.clear()
        self.addItem('Random')
        for name in names :
            self.addItem(name)
    

class OrderSensChoice(QPushButton):
    """Crée un bouton pour choisir le sens de tri : croissant ou décroissant.
    
    - update_screen : fonction de refraîchissement de l'affichage en du sens de tri choisi
    - get_status : retourne l'état actuel du sens de tri 
    - update : met à jour l'affichage du bouton en fonction du sens de tri choisi"""
    def __init__(self,update_screen) -> None:
        super().__init__()
        self.setText("Ascending")
        self.setFixedSize(120, 40)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")

        self.update_screen = update_screen
        self.iconasc = QIcon("codes/UI/Icones/asc.png")
        self.icondsc = QIcon("codes/UI/Icones/dsc.png")
        self.setIcon(self.iconasc)
        self.clicked.connect(self.update)

    def get_satus(self):
        if self.text() == "Ascending":
            return 1
        return 0
    
    def update(self):
        if self.get_satus():
            self.setIcon(self.icondsc)
            self.setText("Descending")
        else :
            self.setIcon(self.iconasc)
            self.setText("Ascending")

        if init : self.update_screen()
    
    def set_asc(self):
        self.setIcon(self.iconasc)
        self.setText("Ascending")

     
class FilterOptionsBar(QHBoxLayout):
    """Barre d'options pour gérer l'affichage de la liste filtrée. Regroupant le choix de la data_base, le nombre d'élément, la colonne et le sens de tri
    
    - upload_screen : fonction de refraîchissement de l'affichage en fonction des options choisies
    - upload_text : fonction de rafraîchissement du texte recherché affiché uniquement
    - update : met à jour le nom des colonnes de tri possibles"""
    def __init__(self,upload_screen,upload_text):
        super().__init__()

        self.choixbdd = BaseDeDonneChoice(upload_screen)
        self.ascgo = OrderSensChoice(upload_text)
        self.sort_column_choice = SortColumnChoice(upload_text)
        self.number_of_element_choice = NumberOfElementChoice(upload_text)
        
        ##
        self.addWidget(self.choixbdd)
        self.addWidget(self.sort_column_choice)
        self.addStretch()
        self.addWidget(self.number_of_element_choice)
        self.addWidget(self.ascgo)

    def update(self):
        self.sort_column_choice.update()
     

class BaseDeDonneChoice(QComboBox):
    """Combo box permettant de choisir la data_base à associer à la recherche
    
    - upload_screen : fonction de refraîchissement de l'affichage en fonction des options choisies
    - on_selection_changed : met à jour les options de l'écran en fonction de la database choisie """
    def __init__(self,upload_screen):
        super().__init__()
        self.setFixedSize(120,40)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.currentIndexChanged.connect(self.on_selection_changed)

        self.upload_screen = upload_screen

        self.addItem('Wines')
        self.addItem('Cocktails')
        self.addItem('Beers')
        self.addItem('Coffees')
        self.addItem('Mocktails')

        
    def on_selection_changed(self,index):
        Db.choix_de_la_data_base = index
        if init : self.upload_screen()
############################################################
#Création du tableau d'affichage
############################################################
class CustomListAffichageTri(QWidget):
    """Classe permettant l'affichage des lignes de la database choisie
    
    - mousePressEvent : détecte le clic de souris sur une des lignes de la database et redirige vers la page de description associée"""
    def __init__(self, completion_text_to_display,indexx, GoToDescription):
        super().__init__()
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.appel_a_description = GoToDescription
        self.indexx = indexx
        layout = QHBoxLayout(self)

        for text in completion_text_to_display:
            text = text.replace('[','').replace(']','').replace("'",'')
            label = QLabel(text)
            label.setAlignment(Qt.AlignCenter)
            label.setWordWrap(True)
            layout.addWidget(label)

        self.setLayout(layout)
        

    def mousePressEvent(self, a0: QMouseEvent) -> None:

        Db.index_boisson = self.indexx
        self.appel_a_description()


class ColumnCategoriesNames(QWidget):
    """Label indiquant à quoi correspondent les données de la colonne associée
    
    - texte : titre de la colonne"""
    def __init__(self,texte):
        super().__init__()

        # Create a QLabel
        label = QLabel(texte, self)

        label.setAlignment(Qt.AlignCenter) 
        label.setStyleSheet("background-color: #1f1f1f; color: #ffffff;")

        layout = QVBoxLayout(self)
        layout.addWidget(label)


class LineOfCategoriesNames(QHBoxLayout):
     """Layout des noms des colonnes mis en ligne"""
     def __init__(self):
        super().__init__()
        self.upload_names()
  
     def upload_names(self):
        titles = Db.dbsall[Db.choix_de_la_data_base][2]
        while self.count():
                item = self.takeAt(0)
                widget = item.widget()
                if widget :
                    widget.deleteLater()
        for title in titles:
            Etiquette = ColumnCategoriesNames(title)
            self.addWidget(Etiquette)


class ColumnOfFilter(QVBoxLayout):
    """Assemblage des filtres sur un layout vertical
    
    - charger_new_df : fonction d'appel pour l'affichage des résultats."""
    def __init__(self,charger_new_df):
        super().__init__()
        self.charger_new_df = charger_new_df
        self.upload_filters()

    def upload_filters(self):
        self.filters_list = RB.from_df_to_filters(self.charger_new_df)
        while self.count():
            item = self.takeAt(0)
            widget = item.widget()
            if widget :
                widget.deleteLater()

        for filter in self.filters_list :
            self.addWidget(filter.name_edit)


############################################################
#Ecran principal
############################################################
class ScreenResearch(QWidget):
    """Assemblage des différents blocs de recherche : filtres, affichage des éléments et options de recherche.
    
    - changer_screen : fonction de rafraîchissement de la page"""
    def __init__(self,change_screen) -> None:
        super().__init__()
        self.setWindowTitle("Description Window")
        self.resize(1000,500)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        
        self.GoToDescription = change_screen

        #Créations des filtres dynamiques
        self.column_of_filter = ColumnOfFilter(self.charger_new_df)
        #Création de la barre d'option pour manipuler les données
        self.optionsdefiltres = FilterOptionsBar(self.upload_screen,self.charger_new_df)
      
        #Création des titres des colonnes des données affichées
        self.Line_Of_Categories_Names = LineOfCategoriesNames()

        #Complétion des layout
        self.listlayout = QVBoxLayout()
        self.listWidget = QListWidget()
        self.listlayout.addLayout(self.Line_Of_Categories_Names)
        self.listlayout.addWidget(self.listWidget)
        
        #Assemblage layout
        descriptionLayout = QHBoxLayout()
        self.screenLayout = QVBoxLayout()

        descriptionLayout.addLayout(self.listlayout,7)
        descriptionLayout.addLayout(self.column_of_filter,3)
        self.screenLayout.addLayout(self.optionsdefiltres)
        self.screenLayout.addLayout(descriptionLayout)
        self.setLayout(self.screenLayout)

        #Remplissage aléaotire pour un premier affichage
        self.upload_screen()
        global init
        init = 1

    def upload_screen(self):
        self.column_of_filter.upload_filters()
        self.optionsdefiltres.update()
        self.charger_new_df()

        self.Line_Of_Categories_Names.upload_names()

    #Charger la df filtrée avec les filtres
    def charger_new_df(self):
        sorting_sens = self.optionsdefiltres.ascgo.get_satus()
        filters_column = self.column_of_filter.filters_list
        sorting_column = self.optionsdefiltres.sort_column_choice.currentText()
        
        number_of_element =  self.optionsdefiltres.number_of_element_choice.currentText()
        indexes,L,textes = RB.from_filters_to_newDF(filters_column,number_of_element,sorting_column,sorting_sens)
        self.changer_text(indexes,L,textes)

    
    ##Gère l'affichage en fonction de tous les éléments choisis
    def changer_text(self,indexes,L,textes):
        #choix du nombre d'éléments

        if len(L) > 0 : self.listWidget.clear()

        for k in range(len(L)):
            listItem = QListWidgetItem(self.listWidget)
            indexx = indexes[k]
            customItemWidget = CustomListAffichageTri(textes[k],indexx,self.GoToDescription)
            listItem.setSizeHint(customItemWidget.sizeHint())
            self.listWidget.addItem(listItem)
            self.listWidget.setItemWidget(listItem, customItemWidget)
            self.listWidget.setStyleSheet("""
            QListWidget::item {
                border: 2px outset #000010; /* Bordure noire d'1px */
                border-radius: 3px; /* Coins arrondis pour la bordure */
            }""")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            filters_column = self.column_of_filter.filters_list
            sorting_column = self.optionsdefiltres.sort_column_choice.currentText()
            sorting_sens = self.optionsdefiltres.ascgo.get_satus()
            number_of_element =  self.optionsdefiltres.number_of_element_choice.currentText()
            indexes,_,_ = RB.from_filters_to_newDF(filters_column,number_of_element,sorting_column,sorting_sens)
            if indexes == [] :
                msg_box = QMessageBox()
                msg_box.setStyleSheet("background-color: #404040; color: #ffffff;")
                msg_box.setWindowTitle("Warning")
                msg_box.setText("No drinks match these filters")
                msg_box.exec_()     
            else : self.charger_new_df()
        else:
            super().keyPressEvent(event)
    

############################################################
############################################################
############################################################
# Test : Les test pour l'interface utilisateur se feront en constatant
        #visuellement si les actions sont effectuées. Les test suivants doivent 
        #être réalisés.
# - 1 : La fenêtre respecte l'affichage du cahier des charges
# - 2 : Les éléments affichés s'actualisent correctement en fonction de la database choisie     
# - 3 : Les éléments affichés s'actualisent correctement en fonction de la colonne de tri et du mode de tri choisi 
# - 4 : Les éléments affichés s'actualisent correctement en fonction des filtres dynamiques utilisés
# - 5 : Les éléments affichés s'actualisent correctement en fonction du nombre d'éléments à afficher choisi
# - 6 : Le message d'erreur "No drinks match these filters" s'affiche correctement si la recherche par filtre dynamique n'a rien donné             
############################################################
############################################################
############################################################
                  
def display_test():
    
    app = QApplication(sys.argv)
    fenetre = ScreenResearch(lambda : 1)
    fenetre.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test = input("Tester les fonctions du script ? (0/1) : ")
    if test : display_test()
    