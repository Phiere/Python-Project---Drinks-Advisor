############################################################
############################################################
############################################################
#DESCRIPTION
############################################################
############################################################
############################################################

import sys
from PyQt5.QtGui import QPixmap, QIcon, QMouseEvent, QStandardItemModel, QStandardItem, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit,QHBoxLayout,QPushButton,QComboBox,QLabel,QListWidget,QListWidgetItem
from PyQt5.QtCore import Qt, QObject, pyqtSignal,QEvent
import random
import Navigation as Nav
sys.path.append('codes/BackEnd/')
import Db_gestions as Db
import Research_page_back as RB 
import Description_page as Dp


### peut être ajouter un bouton "rechercher" pour forcer la recherche et du coup montrer que ya pas


choix_de_la_data_base = 0
index = 0
boisson_choisie = (choix_de_la_data_base,index)
init = 0

#Détecter le signal quand j'appuie sur entrée
##BENE
class KeyEventFilter(QObject):
    enterPressed = pyqtSignal()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
            self.enterPressed.emit()
        return super().eventFilter(obj, event)
    

############################################################
############################################################
##Creer une combobox sur le nombre d'éléments à afficher dans la la liste filtrée
##BENE
class NumberOfElementChoice(QComboBox):
    def __init__(self,upload_screen):
        super().__init__()
        self.setFixedSize(120, 40)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")

        # Ajouter des options arbitraires  à la liste déroulante
        self.addItem('10')
        self.addItem('20')
        self.addItem('50')
        self.addItem('All')
        self.activated[str].connect(upload_screen)

##Creer une combobox sur le noms de la colonne sur laquelle le tri d'affichage sera fait 
##BENE
class SortColumnChoice(QComboBox):
    def __init__(self,upload_screen):
        super().__init__()
        self.activated[str].connect(upload_screen)
        self.setFixedSize(120,40)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")

        ##
        self.update()
       
    def update(self):
        global choix_de_la_data_base
        names = Db.dbsall[choix_de_la_data_base][4] 

        self.clear()
        self.addItem('Random')
        for name in names :
            self.addItem(name)
            
##BENE   
class OrderSensChoice(QPushButton):
    def __init__(self,update_screen) -> None:
        super().__init__()
        self.setText("Croissant")
        self.setFixedSize(120, 40)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")

        self.update_screen = update_screen
        self.iconasc = QIcon("codes/UI/Icones/asc.png")
        self.icondsc = QIcon("codes/UI/Icones/dsc.png")
        self.setIcon(self.iconasc)
        self.clicked.connect(self.update)

    def getSatus(self):
        if self.text() == "Croissant":
            return 1
        return 0
    
    def update(self):
        if self.getSatus():
            self.setIcon(self.icondsc)
            self.setText("Décroissant")
        else :
            self.setIcon(self.iconasc)
            self.setText("Croissant")

        if init : self.update_screen()
    
    
##Barre d'options pour gérer l'affichage de la liste filtrée
##BENE
class FilterOptionsBar(QHBoxLayout):
    def __init__(self,upload_screen) -> None:
        super().__init__()

        self.choixbdd = BaseDeDonneChoice(upload_screen)
        self.ascgo = OrderSensChoice(upload_screen)
        self.sort_column_choice = SortColumnChoice(upload_screen)
        self.number_of_element_choice = NumberOfElementChoice(upload_screen)
        
        ##
        self.addWidget(self.choixbdd)
        self.addWidget(self.sort_column_choice)
        self.addStretch()
        self.addWidget(self.number_of_element_choice)
        self.addWidget(self.ascgo)

    def update(self):
        self.sort_column_choice.update()

    
##BENE
class BaseDeDonneChoice(QComboBox):
    def __init__(self,upload_screen):
        super().__init__()
        self.setFixedSize(120,40)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.currentIndexChanged.connect(self.on_selection_changed)

        self.upload_screen = upload_screen

        self.addItem('Wines')
        self.addItem('Cocktails')
        self.addItem('Beers')
        self.addItem('Coffee')
        self.addItem('Mocktails')
        # Connecter un signal pour détecter le changement de sélection
        
    def on_selection_changed(self,index):
        global choix_de_la_data_base
        choix_de_la_data_base = index
        if init : self.upload_screen()
############################################################
############################################################
##Creer l'affichage de tous les éléments trier comme des texte_edits. CLairement c'est le points à modifier les

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
        global index
        index = self.indexx
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
        
        global choix_de_la_data_base
        titles = Db.dbsall[choix_de_la_data_base][2]

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
    def __init__(self,data_frame,chargerNewDf):
        super().__init__()
    
        self.filters_list = RB.from_df_to_filters(data_frame,chargerNewDf)

    def upload_filters(self,data_frame,chargerNewDf):
        global choix_de_la_data_base
    
        self.filters_list = RB.from_df_to_filters(Db.choisir_db(choix_de_la_data_base,1),chargerNewDf)
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

        global choix_de_la_data_base
        self.data_frame = Db.choisir_db(choix_de_la_data_base,0)
        #Créations des filtres dynamique
        self.column_of_filter = ColumnOfFilter(self.data_frame,self.chargerNewDf)
        #Création de la barre d'option pour manipuler les données
        self.optionsdefiltres = FilterOptionsBar(self.upload_screen)
        self.etat = True
        #global choix_de_la_data_base
        
        self.column_of_filter.upload_filters(self.data_frame,self.chargerNewDf)

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
        self.chargerNewDf()
        #self.changer_text(Db.dbsall[choix_de_la_data_base][0])
        global init
        init = 1

    def upload_screen(self):
        
        global choix_de_la_data_base
        self.data_frame = Db.choisir_db(choix_de_la_data_base,0)
        self.column_of_filter.upload_filters(self.data_frame,self.chargerNewDf)
        self.chargerNewDf()
        print('rentré')
        self.optionsdefiltres.update()
        print('sorti')
        self.Line_Of_Categories_Names.upload_names()

    #Charher la df filtrée avec les filtres
    def chargerNewDf(self):
        global choix_de_la_data_base
        frame1 = Db.choisir_db(choix_de_la_data_base,0)
        frame2 = Db.choisir_db(choix_de_la_data_base,2)
        colonne_choose_to_filter = self.optionsdefiltres.sort_column_choice.currentText()
        sens_choose_to_filter = self.optionsdefiltres.ascgo.getSatus()
        tempdf = RB.from_filters_to_newDF(frame1,frame2,self.column_of_filter.filters_list,colonne_choose_to_filter,sens_choose_to_filter)
        self.changer_text(tempdf)

    
    ##Gere l'affichage en fonction de tous les éléments choisis
    def changer_text(self,newdf):
        #choix du nombre d'éléments

        choix = self.optionsdefiltres.number_of_element_choice.currentText()
        n=0
        if choix == 'All' :
            n = len(newdf)
        else :
            n = int(self.optionsdefiltres.number_of_element_choice.currentText())
        

        if not(newdf.empty) and len(newdf) > n:
            self.listWidget.clear()
            random_or_not = self.optionsdefiltres.sort_column_choice.currentText()
            if random_or_not == 'Random':
                L = random.sample(range(0, len(newdf)), n)
            else :   
                L = range(0,n)
            for i in L:
                listItem = QListWidgetItem(self.listWidget)
                texte = [str(newdf.iat[i,j]) for j in range(len(newdf.columns))]
                global choix_de_la_data_base
                indexx = int(Db.dbsall[choix_de_la_data_base][0].iat[i,0])
                customItemWidget = CustomListAffichageTri(texte,indexx,self.GoToDescription)
                listItem.setSizeHint(customItemWidget.sizeHint())
                self.listWidget.addItem(listItem)
                self.listWidget.setItemWidget(listItem, customItemWidget)

     
        
        elif not(newdf.empty) :

            self.listWidget.clear()

            for i in range(len(newdf)):  
                listItem = QListWidgetItem(self.listWidget)
                texte = [str(newdf.iat[i,j]) for j in range(len(newdf.columns))]
   
                index = int(Db.dbsall[choix_de_la_data_base][0].iat[i,0])
                customItemWidget = CustomListAffichageTri(texte,self.GoToDescription)
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
    