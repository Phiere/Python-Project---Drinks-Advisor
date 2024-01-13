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


### peut être ajouter un bouton "rechercher" pour forcer la recherche et du coup montrer que ya pas

dbs = Db.choix_db("Cocktail")

#détecter le signal quand j'appuie sur entrée
class KeyEventFilter(QObject):
    enterPressed = pyqtSignal()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
            self.enterPressed.emit()
        return super().eventFilter(obj, event)
    
##Creer une combobox sur le nombre d'éléments à afficher dans la la liste filtrée
class NumberOfElementChoice(QComboBox):
    def __init__(self,layout_interaction):
        super().__init__()
        
        # Ajouter des options à la liste déroulante
        self.addItem('10')
        self.addItem('20')
        self.addItem('50')
        self.addItem('All')

        self.setFixedSize(100, 30)
        self.activated[str].connect(layout_interaction)


##Creer une combobox sur le noms de la colonne sur laquelle le tri d'affichage sera fait 
class SortColumnChoice(QComboBox):
    def __init__(self,columns_names_list,layout_interaction) -> None:
        super().__init__()

        ##
        for i in range(1,len(columns_names_list)):
            self.addItem(columns_names_list[i])

        self.setFixedSize(100, 30)
        self.activated[str].connect(layout_interaction)


##Barre d'options pour gérer l'affichage de la liste filtrée
class FilterOptionsBar(QHBoxLayout):
    def __init__(self,ecran,data_frame) -> None:
        super().__init__()

        self.choixbdd = BaseDeDonneChoice()

        self.rdchoice = QPushButton()
        self.empty_random_icon = QIcon("codes/UI/Icones/random_empty.png") 
        self.rdchoice.setIcon(self.empty_random_icon)
        self.rdchoice.setFixedSize(30, 30)
        self.is_rdc = False

        self.ascIcon = QIcon("codes/UI/Icones/asc.png")
        self.ascgo = QPushButton("Croissant")
        self.ascgo.setIcon(self.ascIcon)
        self.ascgo.setFixedSize(100, 30)
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

##Creer l'affichage de tous les éléments trier comme des texte_edits. CLairement c'est le points à modifier les
##text edit vont pas du tout.
class CustomListAffichageTri(QWidget):
    def __init__(self,data_base_utilisee,index_element,completion_text_to_display,GoToDescription):
        super().__init__()

        self.appel_a_description = GoToDescription

        self.db = data_base_utilisee
        self.ind = index_element

        layout = QHBoxLayout(self)
        ## Créer des zones de textes pour chaque éléments (temporaire, faudra faire plus beau la c'est des texte basiques)
      
        for i in range(len(completion_text_to_display)):
            lineEdit = QLineEdit()
            lineEdit.setText(completion_text_to_display[i])
            layout.addWidget(lineEdit)
    
    def mousePressEvent(self, a0: QMouseEvent) -> None:
        print('appel  à la page décription', self.ind)
        self.appel_a_description()

class ColumnCategoriesNames(QWidget):
    def __init__(self,texte):
        super().__init__()

        # Create a QLabel
        label = QLabel(texte, self)

        label.setAlignment(Qt.AlignCenter) 
        label.setStyleSheet("QLabel { color: black; background-color: lightgray; }")

        layout = QVBoxLayout(self)
        layout.addWidget(label)
       
class LineOfCategoriesNames(QWidget):
     def __init__(self,pertinent_columns_names):
        super().__init__()

        self.layout_category_names = QHBoxLayout()

        for i in range(1,len(pertinent_columns_names)):
            Etiquette = ColumnCategoriesNames(pertinent_columns_names[i])
            self.layout_category_names.addWidget(Etiquette)

class BaseDeDonneChoice(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.dropdown = QComboBox(self)
        self.dropdown .addItem('Wines')
        self.dropdown .addItem('Cocktails')
        self.dropdown .addItem('Beers')
        self.dropdown .addItem('Coffee')
        self.dropdown .addItem('Mocktails')

        # Connecter un signal pour détecter le changement de sélection
        self.dropdown .currentIndexChanged.connect(self.on_selection_changed)

        self.setFixedSize(100, 30)

    def on_selection_changed(self,index):
        pass

##Creation de l'écran
class ScreenResearch(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Description Window")
        self.resize(1000,500)

        self.GoToDescription = lambda : 1
        ##Cette info viendra de la page d'acceuil
        self.data_frame = dbs[1]

        #Création des layouts généraux
 
        descriptionLayout = QHBoxLayout()
        self.filtresLayout = QVBoxLayout()
        self.screenLayout = QVBoxLayout()
        
        #Ajout des filtres dynamiques
        self.filters_list = RB.from_df_to_filters(self.data_frame,self.chargerNewDf)

        for i in range(len(self.filters_list)):
             self.filtresLayout.addWidget(self.filters_list[i].name_edit)


        #je veux déclanger une recherche en appuant sur entrée.
             
        self.key_event_filter = KeyEventFilter()
        QApplication.instance().installEventFilter(self.key_event_filter)

        # Connecter le signal du filtre d'événements à la fonction que vous souhaitez déclencher
        self.key_event_filter.enterPressed.connect(self.chargerNewDf)
        
        self.optionsdefiltres = FilterOptionsBar(self,self.data_frame)
        self.etat = True

        Line_Of_Categories_Names = LineOfCategoriesNames(dbs[3])

        #Complétion des layout
        self.listlayout = QVBoxLayout()
        self.listWidget = QListWidget()
        self.listlayout.addLayout(Line_Of_Categories_Names.layout_category_names)
        self.listlayout.addWidget(self.listWidget)
        #self.listWidget.setMinimumSize(QSize(600,500))

        #remplissage aléaotire pour un premier affichage
        self.changer_text(dbs[1][dbs[3]])

        #Assemblage layout
        descriptionLayout.addLayout(self.listlayout,8)
        descriptionLayout.addLayout(self.filtresLayout,2)
        self.screenLayout.addLayout(self.optionsdefiltres)
        self.screenLayout.addLayout(descriptionLayout)
        self.setLayout(self.screenLayout)
        


    #Charher la df filtrée avec les filtres
    def chargerNewDf(self):
        tempdf = RB.from_filters_to_newDF(self.data_frame,self.filters_list,self.optionsdefiltres.ascchoice.comboBox.currentText(),self.etat)
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
                customItemWidget = CustomListAffichageTri(dbs[0],newdf.iat[i,0],texte,self.GoToDescription)
                listItem.setSizeHint(customItemWidget.sizeHint())
                self.listWidget.addItem(listItem)
                self.listWidget.setItemWidget(listItem, customItemWidget)
            #self.listlayout.updae()
     
        
        elif not(newdf.empty) :

            self.listWidget.clear()

            for i in range(len(newdf)):  
                listItem = QListWidgetItem(self.listWidget)
                texte = [str(newdf.iat[i,j]) for j in range(1,len(newdf.columns))]
                customItemWidget = CustomListAffichageTri(dbs[0],newdf.iat[i,0],texte,self.GoToDescription)
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
                
def testeur():
    pass

            
def main():
    app = QApplication(sys.argv)
    fenetre = ScreenResearch()
    fenetre.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    