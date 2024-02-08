############################################################
############################################################
############################################################
#DESCRIPTION
############################################################
############################################################
############################################################

import sys
from PyQt5.QtGui import QIcon, QMouseEvent
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout,QPushButton,QComboBox,QLabel,QListWidget,QListWidgetItem
from PyQt5.QtCore import Qt, QObject, pyqtSignal,QEvent
sys.path.append('codes/BackEnd/')
import Db_gestions as Db
import Research_page_back as RB 


### peut être ajouter un bouton "rechercher" pour forcer la recherche et du coup montrer que ya pas

init = 0

#V0.1
class KeyEventFilter(QObject):
    """Déclanche une action lorsqu'on appuie sur entrée"""
    enterPressed = pyqtSignal()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
            self.enterPressed.emit()
        return super().eventFilter(obj, event)
    

############################################################
############################################################
#V0.1
class NumberOfElementChoice(QComboBox):
    """Combo box permettant de choisir le nombre d'éléments à afficher.
    
    - upload_screen : fonction de refraichissement de l'affichage en fonction du nombre d'éléments choisi
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

#V0.1
class SortColumnChoice(QComboBox):
    """Creer une combobox sur le noms de la colonne sur laquelle le tri d'affichage sera fait 
    
    - upload_screen : fonction de refraichissement de l'affichage en fonction de la colonne de tri choisi
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
            
#V0.1
class OrderSensChoice(QPushButton):
    """Créer un bouton pour choisir le sens de tri : croissant ou décroissant.
    
    - update_screen : fonction de refraichissement de l'affichage en du sens de tri choisi
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
    
    
##Barre d'options pour gérer l'affichage de la liste filtrée
#V0.1
class FilterOptionsBar(QHBoxLayout):
    """Barre d'options pour gérer l'affichage de la liste filtrée. Regroupant le choix de la data_base, le nombre d'élement, la colonne et le sens de tri
    
    - upload_screen : fonction de refraichissement de l'affichage en fonction des options choisies
    - upload_text : fonction de rafraichissement du texte recherché affiché uniquement
    - update : met à jour le noms des colonnes de tri possibles"""
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

    
#V0.1
class BaseDeDonneChoice(QComboBox):
    """Combo box permettant de choisir la data_base à associer à la rehcehr
    
    - upload_screen : fonction de refraichissement de l'affichage en fonction des options choisies
    - on_selection_changed : met à jours les options de l'écran en fonction de la database choisie """
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
############################################################

#V0.0
class CustomListAffichageTri(QWidget):
    def __init__(self, completion_text_to_display,indexx, GoToDescription):
        super().__init__()
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.appel_a_description = GoToDescription
        self.indexx = indexx
        layout = QHBoxLayout(self)

        for text in completion_text_to_display:
            label = QLabel(text)
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)

        self.setLayout(layout)

    def mousePressEvent(self, a0: QMouseEvent) -> None:

        Db.index_boisson = self.indexx
        self.appel_a_description()

##
class ColumnCategoriesNames(QWidget):
    def __init__(self,texte):
        super().__init__()

        # Create a QLabel
        label = QLabel(texte, self)

        label.setAlignment(Qt.AlignCenter) 
        label.setStyleSheet("background-color: #1f1f1f; color: #ffffff;")

        layout = QVBoxLayout(self)
        layout.addWidget(label)

##       
class LineOfCategoriesNames(QHBoxLayout):
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

##
class ColumnOfFilter(QVBoxLayout):
    def __init__(self,chargerNewDf):
        super().__init__()
        self.chargerNewDf = chargerNewDf
        self.upload_filters()

    def upload_filters(self):
        self.filters_list = RB.from_df_to_filters(self.chargerNewDf)
        while self.count():
            item = self.takeAt(0)
            widget = item.widget()
            if widget :
                widget.deleteLater()

        for filter in self.filters_list :
            self.addWidget(filter.name_edit)

############################################################
############################################################
##Creation de l'écran
class ScreenResearch(QWidget):
    def __init__(self,change_screen) -> None:
        super().__init__()
        self.setWindowTitle("Description Window")
        self.resize(1000,500)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        
        self.GoToDescription = change_screen

        #Créations des filtres dynamique
        self.column_of_filter = ColumnOfFilter(self.chargerNewDf)
        #Création de la barre d'option pour manipuler les données
        self.optionsdefiltres = FilterOptionsBar(self.upload_screen,self.chargerNewDf)

        #Déclenger une recherche avec le bouton entrée
        self.key_event_filter = KeyEventFilter()
        QApplication.instance().installEventFilter(self.key_event_filter)
        self.key_event_filter.enterPressed.connect(self.chargerNewDf)
        
        #Créations des titres des colonnes des données affichées
        self.Line_Of_Categories_Names = LineOfCategoriesNames()

        #Complétion des layout
        self.listlayout = QVBoxLayout()
        self.listWidget = QListWidget()
        self.listlayout.addLayout(self.Line_Of_Categories_Names)
        self.listlayout.addWidget(self.listWidget)
        
        #Assemblage layout
        descriptionLayout = QHBoxLayout()
        self.screenLayout = QVBoxLayout()

        descriptionLayout.addLayout(self.listlayout,8)
        descriptionLayout.addLayout(self.column_of_filter,2)
        self.screenLayout.addLayout(self.optionsdefiltres)
        self.screenLayout.addLayout(descriptionLayout)
        self.setLayout(self.screenLayout)

        #remplissage aléaotire pour un premier affichage
        self.upload_screen()
        global init
        init = 1

    def upload_screen(self):
        self.column_of_filter.upload_filters()
        self.optionsdefiltres.update()
        self.chargerNewDf()

        self.Line_Of_Categories_Names.upload_names()

    #Charher la df filtrée avec les filtres
    def chargerNewDf(self):
        filters_column = self.column_of_filter.filters_list
        sorting_column = self.optionsdefiltres.sort_column_choice.currentText()
        sorting_sens = self.optionsdefiltres.ascgo.get_satus()
        number_of_element =  self.optionsdefiltres.number_of_element_choice.currentText()
        indexes,L,textes = RB.from_filters_to_newDF(filters_column,number_of_element,sorting_column,sorting_sens)
        self.changer_text(indexes,L,textes)

    
    ##Gere l'affichage en fonction de tous les éléments choisis
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

    

############################################################
############################################################
############################################################
# Test : fenêtre sans navigation vers les autres écrans. Les conditions suivantes sont remplies :
# - 1 :
# - 2 :                 
############################################################
############################################################
############################################################
                
            
def main():
    app = QApplication(sys.argv)
    fenetre = ScreenResearch(lambda : 1)
    fenetre.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    