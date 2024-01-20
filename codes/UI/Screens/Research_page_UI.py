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

import Navigation as Nav
sys.path.append('codes/BackEnd/')
import Db_gestions as Db
import Research_page_back as RB 
import Description_page as Dp


### peut être ajouter un bouton "rechercher" pour forcer la recherche et du coup montrer que ya pas

dbs = Db.dbs

choix_de_la_data_base = 0

boisson_choisie = []

#Détecter le signal quand j'appuie sur entrée
class KeyEventFilter(QObject):
    enterPressed = pyqtSignal()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
            self.enterPressed.emit()
        return super().eventFilter(obj, event)
    

############################################################
############################################################
##Creer une combobox sur le nombre d'éléments à afficher dans la la liste filtrée
class NumberOfElementChoice(QComboBox):
    def __init__(self,layout_interaction):
        super().__init__()

        # Ajouter des options à la liste déroulante
        self.addItem('10')
        self.addItem('20')
        self.addItem('50')
        self.addItem('All')

        self.setFixedSize(120, 40)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.activated[str].connect(layout_interaction)

##Creer une combobox sur le noms de la colonne sur laquelle le tri d'affichage sera fait 
class SortColumnChoice(QComboBox):
    def __init__(self,columns_names_list,layout_interaction) -> None:
        super().__init__()

        ##
        for i in range(1,len(columns_names_list)):
            self.addItem(columns_names_list[i])

        self.activated[str].connect(layout_interaction)
        self.setFixedSize(120,40)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")

    def update_sort(self):
        pass
        #ew_sorted_choice = RB.chose_sorted_sens(self.optionsdefiltres.ascgo.text())
        #self.optionsdefiltres.ascgo.setText(new_sorted_choice)

##Barre d'options pour gérer l'affichage de la liste filtrée
class FilterOptionsBar(QHBoxLayout):
    def __init__(self,ecran,data_frame,db_choice,upload_screen) -> None:
        super().__init__()

        self.choixbdd = BaseDeDonneChoice(db_choice,upload_screen)
        
        self.rdchoice = QPushButton()
        self.empty_random_icon = QIcon("codes/UI/Icones/random_empty.png") 
        self.rdchoice.setIcon(self.empty_random_icon)
        self.rdchoice.setFixedSize(40, 40)
        self.rdchoice.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.is_rdc = False

        self.ascIcon = QIcon("codes/UI/Icones/asc.png")
        self.ascgo = QPushButton("Croissant")
        self.ascgo.setIcon(self.ascIcon)
        self.ascgo.setFixedSize(120, 40)
        self.ascgo.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.is_asc = False

        ##
        self.sort_column_choice = SortColumnChoice(data_frame.columns,ecran.chargerNewDf)
        self.number_of_element_choice = NumberOfElementChoice(ecran.chargerNewDf)
        
        ##
        self.addWidget(self.choixbdd)
        self.addWidget(self.sort_column_choice)
        self.addStretch()
        self.addWidget(self.number_of_element_choice)
        self.addWidget(self.ascgo)
        self.addWidget(self.rdchoice)

        self.ascgo.clicked.connect(ecran.changersens)
        self.rdchoice.clicked.connect(self.toggle_rdc)

    def get_text_combo_box(self,combo_box):
        if combo_box == "nb_of_elements" :
            return self.number_of_element_choice.currentText()
        else :
            return 0
        
    def toggle_rdc(self):
        # Fonction appelée lors du clic sur le bouton "Ajouter en favori"
        filled_random_icon = QIcon("codes/UI/Icones/random_filled.png")

        self.is_rdc = not self.is_rdc  # Inverser le statut du favori

        # Changer l'icône du bouton en fonction du statut du favori
        if self.is_rdc:
            self.rdchoice.setIcon(filled_random_icon)
        else:
            self.rdchoice.setIcon(self.empty_random_icon)

##
class BaseDeDonneChoice(QComboBox):
    def __init__(self,db_choice,upload_screen):
        super().__init__()

        self.fonction = upload_screen

        self.db_choice = db_choice
        self.addItem('Wines')
        self.addItem('Cocktails')
        self.addItem('Beers')
        self.addItem('Coffee')
        self.addItem('Mocktails')

        self.setFixedSize(120,40)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        # Connecter un signal pour détecter le changement de sélection
        self.currentIndexChanged.connect(self.on_selection_changed)

        
    def on_selection_changed(self,index):
        global choix_de_la_data_base
        choix_de_la_data_base = index
        self.fonction()
############################################################
############################################################
##Creer l'affichage de tous les éléments trier comme des texte_edits. CLairement c'est le points à modifier les

class CustomListAffichageTri(QWidget):
    def __init__(self, data_base_utilisee, index_element, completion_text_to_display, GoToDescription):
        super().__init__()

        self.appel_a_description = GoToDescription
        self.db = data_base_utilisee
        self.ind = index_element

        layout = QHBoxLayout(self)

        for i in range(len(completion_text_to_display)):
            label = QLabel(completion_text_to_display[i])
            
            # Centrer horizontalement pour toutes les colonnes
            label.setAlignment(Qt.AlignCenter)
            
            layout.addWidget(label)

        self.setLayout(layout)

        # Définir le style CSS pour le fond et le texte
        self.setStyleSheet("background-color: #404040; color: #ffffff;")

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        global boisson_choisie

        boisson_choisie = self.db.iloc[self.ind]
        print('Appel à la page description', self.ind)
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
        pertinent_columns_names = Db.choisir_db(choix_de_la_data_base,3)

        while self.count():
                item = self.takeAt(0)
                widget = item.widget()
                if widget :
                    widget.deleteLater()

        for i in range(1,len(pertinent_columns_names)):
            Etiquette = ColumnCategoriesNames(pertinent_columns_names[i])
            self.addWidget(Etiquette)

##
class ColumnOfFilter(QVBoxLayout):
    def __init__(self,data_frame,chargerNewDf):
        super().__init__()
    
        self.filters_list = RB.from_df_to_filters(data_frame,chargerNewDf)

    def upload_filters(self,data_frame,chargerNewDf):
        global choix_de_la_data_base
    
        self.filters_list = RB.from_df_to_filters(data_frame,chargerNewDf)
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

    
        #global choix_de_la_data_base
        global choix_de_la_data_base
        self.data_frame = Db.choisir_db(choix_de_la_data_base,1)

        #Création de la barre d'option pour manipuler les données
        self.optionsdefiltres = FilterOptionsBar(self,self.data_frame,choix_de_la_data_base,self.upload_screen)
        self.etat = True
        
        #Créations des filtres dynamique
        self.column_of_filter = ColumnOfFilter(self.data_frame,self.chargerNewDf)
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
        self.changer_text(Db.choisir_db(choix_de_la_data_base,1)[Db.choisir_db(choix_de_la_data_base,3)])
        
    def upload_screen(self):
        global choix_de_la_data_base
        self.data_frame = Db.choisir_db(choix_de_la_data_base,2)
        self.column_of_filter.upload_filters(self.data_frame,self.chargerNewDf)
        self.chargerNewDf()
        self.Line_Of_Categories_Names.upload_names()

    #Charher la df filtrée avec les filtres
    def chargerNewDf(self):
        global choix_de_la_data_base
        frame1 = Db.choisir_db(choix_de_la_data_base,1)
        frame2 = Db.choisir_db(choix_de_la_data_base,3)
        tempdf = RB.from_filters_to_newDF(frame1,frame2,self.column_of_filter.filters_list)#,self.optionsdefiltres.ascchoice.comboBox.currentText(),self.etat)
        self.changer_text(tempdf)


    ##Pour choisir si l'affichage se fera en croissant ou décroissant
    def changersens(self):
        new_sorted_choice = RB.chose_sorted_sens(self.optionsdefiltres.ascgo.text())
        self.optionsdefiltres.ascgo.setText(new_sorted_choice)
        self.etat=not(self.etat)
        #self.chargerNewDf()
        dscIcon = QIcon("codes/UI/Icones/dsc.png")
        self.optionsdefiltres.is_asc = not self.optionsdefiltres.is_asc
        if self.optionsdefiltres.is_asc:
            self.optionsdefiltres.ascgo.setIcon(dscIcon)
        else:
            self.optionsdefiltres.ascgo.setIcon(self.optionsdefiltres.ascIcon)
    
    ##Gere l'affichage en fonction de tous les éléments choisis
    def changer_text(self,newdf):
        #choix du nombre d'éléments

        choix = self.optionsdefiltres.get_text_combo_box("nb_of_elements")
        n=0
        if choix == 'All' :
            n = len(newdf)
        else :
            n = int(self.optionsdefiltres.get_text_combo_box("nb_of_elements")) 
        

        if not(newdf.empty) and len(newdf) > n:
            self.listWidget.clear()

            for i in range(n):# Exemple avec 10 éléments
                listItem = QListWidgetItem(self.listWidget)
                texte = [str(newdf.iat[i,j]) for j in range(1,len(newdf.columns))]
                global choix_de_la_data_base
                #index_element = Db.choisir_db(choix_de_la_data_base,0)[0,i]
                index = newdf.loc[i].index
                customItemWidget = CustomListAffichageTri(Db.choisir_db(choix_de_la_data_base,0),int(newdf.iat[i,0]),texte,self.GoToDescription)
                listItem.setSizeHint(customItemWidget.sizeHint())
                self.listWidget.addItem(listItem)
                self.listWidget.setItemWidget(listItem, customItemWidget)

     
        
        elif not(newdf.empty) :

            self.listWidget.clear()

            for i in range(len(newdf)):  
                listItem = QListWidgetItem(self.listWidget)
                texte = [str(newdf.iat[i,j]) for j in range(1,len(newdf.columns))]
                customItemWidget = CustomListAffichageTri(Db.choisir_db(choix_de_la_data_base,0),int(newdf.iat[i,0]),texte,self.GoToDescription)
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
    