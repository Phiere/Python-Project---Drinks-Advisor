############################################################
############################################################
############################################################
#Construction de la page correspondant au profil de l'utilisateur. 
############################################################
############################################################
############################################################

import sys
import seaborn as sns
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QFrame,QGridLayout,QHBoxLayout,QLabel,QListWidgetItem,QListWidget
from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtCore import QSize, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

sys.path.append('codes/BackEnd/')
import Profil_page_back as Pb
import Db_gestions as Db

categories = ['Wines', 'Cocktails', 'Beers', 'Coffees', 'Mocktails']

###1er élément (à gauche): Liste des infos des boissons ajoutées aux Favoris
class FavorieDataItem(QHBoxLayout):
    def __init__(self, data):
        super().__init__()

        for text in data:
            label = QLabel(text)
            self.addWidget(label)

        vertical_bar = QFrame()
        vertical_bar.setFrameShape(QFrame.VLine)
        vertical_bar.setFrameShadow(QFrame.Sunken)
        vertical_bar.setLineWidth(2)

        self.addWidget(vertical_bar)

#peut être faire plusieurs classe ? ça m'a l'air brouillon ou alors ça serait du forcing
class FavoriesTitle(QHBoxLayout):
    def __init__(self):
        super().__init__()
        image_label = QLabel()
        pixmap = QPixmap("codes/UI/Icones/star_filled.png")
        pixmap = pixmap.scaledToHeight(100) 
        image_label.setPixmap(pixmap)
        image_label.setStyleSheet("border: 2px solid white;")

        # Titre "Boissons Favories"
        title_label = QLabel("Favorite Drinks")
        title_label.setStyleSheet("color: white; font-size: 18px;")

        # Sous-titre "Nombre de boissons"
        self.nb_favories_label = QLabel(f"{0} drink")
        self.nb_favories_label.setStyleSheet("color: white; font-size: 12px;")

        # Layout vertical pour aligner les titres et sous-titres
        title_layout = QVBoxLayout()
        title_layout.addWidget(title_label)
        title_layout.addWidget(self.nb_favories_label)
        title_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        # Construction du main_layout
        self.addWidget(image_label)
        self.addLayout(title_layout)
        self.addStretch()

    def update(self,nb_favories):
            self.nb_favories_label.setText(f"{nb_favories} drinks")

#################
#tableau des favoris
#################
class FavorieDataDisplay(QVBoxLayout):
    def __init__(self,go_to_description):
        super().__init__()

        self.init = 1
        self.go_to_description = go_to_description
        self.title_widget = FavoriesTitle()
        self.listWidget = QListWidget()
        self.categories_names = LineOfCategoriesNames()
        self.addLayout(self.title_widget)
        self.addLayout(self.categories_names)
        self.addWidget(self.listWidget)
    
    def update(self) -> None:
        # Ajouter les éléments de la liste
        favories_dfs = Pb.favorites_extraction()
        nb_favories = len(favories_dfs)
        self.title_widget.update(nb_favories=nb_favories)

        
        if nb_favories > 0:
            self.listWidget.clear()
            for i in range(len(favories_dfs)) :
                listItem = QListWidgetItem(self.listWidget)
                texte = [str(favories_dfs.iat[i,j]) for j in range(len(['Nom_db','Names','personnal_rating','oui']))]                
                indexx = favories_dfs.iat[i,-1]
                customItemWidget = CustomListAffichageTri(texte,indexx,self.go_to_description)
                listItem.setSizeHint(customItemWidget.sizeHint())
                self.listWidget.addItem(listItem)
                self.listWidget.setItemWidget(listItem, customItemWidget)


        elif self.init  :
            listItem = QListWidgetItem(self.listWidget)              
            no_favories_label = QLabel("No drinks were added to Favorites")
            no_favories_label.setAlignment(Qt.AlignCenter)  # Centre le texte horizontalement
            no_favories_label.setStyleSheet("font-size: 10pt;")  # Définit la police à 10pt
            #customItemWidget = CustomListAffichageTri(texte,indexx)#,self.GoToDescription)
            listItem.setSizeHint(no_favories_label.sizeHint())
            self.listWidget.addItem(listItem)
            self.listWidget.setItemWidget(listItem, no_favories_label)
            '''no_favories_label = QLabel("No drinks were added to Favorites")
            no_favories_label.setAlignment(Qt.AlignCenter)  # Centre le texte horizontalement
            no_favories_label.setStyleSheet("font-size: 12pt;")  # Définit la police à 12pt
            self.listWidget.addItem(no_favories_label)
            self.setStretchFactor(no_favories_label, 3) '''
            self.init = 0


class CustomListAffichageTri(QWidget):
    def __init__(self, completion_text_to_display,indexx,go_to_description):
        super().__init__()
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.appel_a_description = go_to_description
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


class ColumnCategoriesNames(QWidget):
    def __init__(self,texte):
        super().__init__()

        # Create a QLabel
        label = QLabel(texte, self)

        label.setAlignment(Qt.AlignCenter) 
        label.setStyleSheet("background-color: #1f1f1f; color: #ffffff;")

        layout = QVBoxLayout(self)
        layout.addWidget(label)


class LineOfCategoriesNames(QHBoxLayout):
     def __init__(self):
        super().__init__()
        self.upload_names()
  
     def upload_names(self):
        titles = ['Db','Names','Personnal Rating','Commentary']
        while self.count():
                item = self.takeAt(0)
                widget = item.widget()
                if widget :
                    widget.deleteLater()
        for title in titles:
            Etiquette = ColumnCategoriesNames(title)
            self.addWidget(Etiquette)


#################
#1er graphique : Histogramme du nombre de boissons notées par catégorie
#################
class RatedByCategories(QWidget):
    def __init__(self):
        super().__init__()

        # Créer un canevas pour le graphique
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.figure, self.ax = plt.subplots()
        self.figure.set_facecolor('#1f1f1f')  
        self.canvas = FigureCanvas(self.figure)
        layout = QGridLayout(self)
        layout.addWidget(self.canvas)

        self.update()
        #self.values = [12, 50, 32, 2, 3] #pour l'exemple

    def update(self):
        self.ax.clear()

        self.values = Pb.nb_notes_per_categories()

        if all(value == 0 for value in self.values):
            self.ax.text(0.5, 0.5, "No drinks were rated", ha='center', va='center', fontsize=12, color='white')
        else:
            sns.barplot(x=categories, y=self.values, palette="viridis", ax=self.ax, edgecolor='white', linewidth=1.5, dodge=False)
        
        self.ax.set_title('Distribution of the number of rated drinks per category', color='white', fontsize=10)
        self.ax.set_ylabel('Number of drinks')
        self.ax.set_facecolor('#1f1f1f')
        
        # Définir la couleur du texte sur les axes
        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.tick_params(axis='both', colors='white')

        for spine in self.ax.spines.values():
                spine.set_edgecolor('white')

        self.canvas.draw()


#################
#2ème graphique : Histogramme des moyennes des notes par catégorie
#################     
class MeanByCategories(QWidget):
    def __init__(self):     
        super().__init__()
        
        # Créer un canevas pour le graphique
        self.setStyleSheet("background-color: #1f1f1f; color: #ffffff;")
        self.figure, self.ax = plt.subplots()
        self.figure.set_facecolor('#1f1f1f') 
        self.canvas = FigureCanvas(self.figure)
        layout = QGridLayout(self)
        layout.addWidget(self.canvas)
        
        self.update()

    def update(self):
        self.ax.clear()

        self.values = Pb.mean_notes_per_categories()

        if all(value == 0 for value in self.values):
            self.ax.text(0.5, 0.5, "No drinks were rated", ha='center', va='center', fontsize=12, color='white')
        else:
            sns.barplot(x=categories, y=self.values, palette="viridis", ax=self.ax, edgecolor='white', linewidth=1.5, dodge=False)
            

        self.ax.set_title('Average drink ratings per category', color='white', fontsize=10)
        self.ax.set_ylabel('Average rating')
        self.ax.set_facecolor('#1f1f1f')

        # Définir la couleur du texte sur l'axe
        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.tick_params(axis='both', colors='white')

        for spine in self.ax.spines.values():
                spine.set_edgecolor('white')

        self.canvas.draw()


#################
#création de l'écran
################# 

class ScreenProfile(QWidget):
    def __init__(self,go_to_description) -> None:
        super().__init__()
        self.setStyleSheet("background-color: #1f1f1f; color: #ffffff;")
        self.setWindowTitle("Profile Window")
        self.resize(1000,500)

        self.rated_by_categories = RatedByCategories()
        self.mean_by_categories_graph = MeanByCategories()
        self.favorie_data_diplay = FavorieDataDisplay(go_to_description=go_to_description)
        graphiques_layout = QVBoxLayout()
        ecran_layout = QHBoxLayout()
        self.update()

        graphiques_layout.addWidget(self.rated_by_categories)
        graphiques_layout.addWidget(self.mean_by_categories_graph)
        

        ecran_layout.addLayout(self.favorie_data_diplay,5)
        ecran_layout.addLayout(graphiques_layout,5)

        self.setLayout(ecran_layout)
        
    def update(self):
        self.favorie_data_diplay.update()
        self.rated_by_categories.update()
        self.mean_by_categories_graph.update()

        
        
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
    fenetre = ScreenProfile()
    fenetre.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    