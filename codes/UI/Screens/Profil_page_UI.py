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
from PyQt5.QtCore import QSize
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

sys.path.append('codes/BackEnd/')
import Profil_page_back as Pb

categories = ['Wines', 'Cocktails', 'Beers', 'Coffees', 'Mocktails']

###1er élément (à gauche): Liste des infos des boissons ajoutées aux Favoris
class FavorieDataLine(QWidget):
    def __init__(self,textes_a_afficher):
        super().__init__()
        self.setStyleSheet("background-color: #1f1f1f; color: #ffffff;")
        self.hbox = QHBoxLayout(self)

        label_list = []
        for text in textes_a_afficher :
            label_list.append(QLabel(text))

        vertical_bar = QFrame()
        vertical_bar.setFrameShape(QFrame.VLine)
        vertical_bar.setFrameShadow(QFrame.Sunken)
        vertical_bar.setLineWidth(2)  # Ajustez la largeur de la barre ici

        for label in label_list :
            self.hbox.addWidget(label)
            self.hbox.addWidget(vertical_bar)
 
class FavorieDataDisplay(QListWidget):
    def __init__(self):
        super().__init__()

        favories_dfs = Pb.favorites_extraction()
        categories = ['Wines', 'Cocktails', 'Beers', 'Coffees', 'Mocktails']

        if not(all(value == 0 for value in favories_dfs)):
            for j in range(len(favories_dfs)) :
                favorie_df = favories_dfs[j]
                for i in range(len(favorie_df)):

                    listItem = QListWidgetItem(self)
                    ligne = favorie_df.iloc[i]
                    element_ligne = [str(e) for e in ligne]
                    element_ligne.append(categories[j])

                    favorie_data_line = FavorieDataLine(element_ligne)
                    listItem.setSizeHint(favorie_data_line.sizeHint())
                    self.addItem(listItem)
                    self.setItemWidget(listItem, favorie_data_line)
        else:
            listItem = "Aucune boisson n'a été ajoutée aux Favoris"
            self.addItem(listItem)

###2ème élément : Espace avec 2 graphiques
###1er graphique : Histogramme du nombre de boissons notées par catégorie
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
            self.ax.text(0.5, 0.5, "Aucune boisson n'a été notée", ha='center', va='center', fontsize=12, color='white')
        else:
            sns.barplot(x=categories, y=self.values, palette="viridis", ax=self.ax, edgecolor='white', linewidth=1.5, dodge=False)
        
        self.ax.set_title('Répartition du nombre de boissons notées par catégorie', color='white', fontsize=10)
        self.ax.set_ylabel('Nombre de boisson')
        self.ax.set_facecolor('#1f1f1f')
        
        # Définir la couleur du texte sur les axes
        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.tick_params(axis='both', colors='white')

        for spine in self.ax.spines.values():
                spine.set_edgecolor('white')

        self.canvas.draw()
        
###2ème graphique : Histogramme des moyennes des notes par catégorie
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
        #self.values = [4.8, 2.6, 3.2, 2.0, 3.0] #pour l'exemple

    def update(self):
        self.ax.clear()

        self.values = Pb.mean_notes_per_categories()

        if all(value == 0 for value in self.values):
            self.ax.text(0.5, 0.5, "Aucune boisson n'a été notée", ha='center', va='center', fontsize=12, color='white')
        else:
            sns.barplot(x=categories, y=self.values, palette="viridis", ax=self.ax, edgecolor='white', linewidth=1.5, dodge=False)
            

        self.ax.set_title('Notes moyennes des boissons par catégorie', color='white', fontsize=10)
        self.ax.set_ylabel('Note moyenne')
        self.ax.set_facecolor('#1f1f1f')

        # Définir la couleur du texte sur l'axe
        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.tick_params(axis='both', colors='white')

        for spine in self.ax.spines.values():
                spine.set_edgecolor('white')

        self.canvas.draw()

##Création de l'écran
##BENE
class ScreenProfile(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet("background-color: #1f1f1f; color: #ffffff;")
        self.setWindowTitle("Profil Window")
        self.resize(1000,500)

        ##Partie droite avec les graphiques
        self.rated_by_categories = RatedByCategories()
        self.mean_by_categories_graph = MeanByCategories()
        favorie_data_diplay = FavorieDataDisplay()
        graphiques_layout = QVBoxLayout()
        ecran_layout = QHBoxLayout()
        self.update()

        graphiques_layout.addWidget(self.rated_by_categories)
        graphiques_layout.addWidget(self.mean_by_categories_graph)
        
        ecran_layout.addWidget(favorie_data_diplay,5)
        ecran_layout.addLayout(graphiques_layout,5)

        self.setLayout(ecran_layout)
        
    def update(self):
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
    