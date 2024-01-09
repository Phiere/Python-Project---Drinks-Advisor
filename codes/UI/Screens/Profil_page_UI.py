############################################################
############################################################
############################################################
#Construction de la page correspondant au profil de l'utilisateur. 
############################################################
############################################################
############################################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QListWidget,QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

import Navigation as Nav
sys.path.append('codes/BackEnd/')
import Profil_page_back as Pb

categories = ['Vins', 'Cocktails', 'Cafés', 'Mocktails', 'Bières']

class premierGraphique(QWidget):
    def __init__(self):
        super().__init__()

        # Créer un canevas pour le graphique
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout = QGridLayout(self)
        layout.addWidget(self.canvas)

        # Générer des données pour l'exemple
        values = Pb.nb_notes_per_categories()

        # Tracer l'histogramme
        self.ax.bar(categories, values, color='skyblue')
        #self.ax.set_title('Exemple d\'histogramme')
        #self.ax.set_xlabel('Catégories')
        #self.ax.set_ylabel('Valeurs')

        # Mettre à jour le canevas
        self.canvas.draw()

class deuxiemeGraphique(QWidget):
    def __init__(self):
        super().__init__()

        # Créer un canevas pour le graphique
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout = QGridLayout(self)
        layout.addWidget(self.canvas)

        # Générer des données pour l'exemple
        values = Pb.mean_notes_per_categories()

        # Tracer l'histogramme
        self.ax.bar(categories, values, color='skyblue')
        #self.ax.set_title('Exemple d\'histogramme')
        #self.ax.set_xlabel('Catégories')
        #self.ax.set_ylabel('Valeurs')

        # Mettre à jour le canevas
        self.canvas.draw()

class troisiemeGraphique(QWidget):
    def __init__(self):
        super().__init__()

        df_favories = 1
        self.listlayout = QVBoxLayout()
        self.listWidget = QListWidget()

        self.listlayout.addWidget(self.listWidget)
        """
        if not(df_favories.empty) :
            self.listWidget.clear()

            ##faut faire une lsit avec les favories
            
            for i in range(len(df_favories)):# Exemple avec 10 éléments
                listItem = QListWidgetItem(self.listWidget)
                texte = [str(newdf.iat[i,j]) for j in range(len(newdf.columns))]
                customItemWidget = CustomListAffichageTri(texte)
                listItem.setSizeHint(customItemWidget.sizeHint())
                self.listWidget.addItem(listItem)
                self.listWidget.setItemWidget(listItem, customItemWidget)
           """ 

class quatriemeGraphique(QWidget):
    def __init__(self):
        super().__init__()

        # Créer un canevas pour le graphique
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout = QGridLayout(self)
        layout.addWidget(self.canvas)

        # Générer des données pour l'exemple
        values = Pb.favories_per_categories()

        # Tracer l'histogramme
        self.ax.bar(categories, values, color='skyblue')
        #self.ax.set_title('Exemple d\'histogramme')
        #self.ax.set_xlabel('Catégories')
        #self.ax.set_ylabel('Valeurs')

        # Mettre à jour le canevas
        self.canvas.draw()


##Creation de l'écran
class ScreenProfile(QWidget):
    def __init__(self,screens_call) -> None:
        super().__init__()
        self.setWindowTitle("Profil Window")
        self.resize(1000,500)

        ##Cette info viendra de la page d'acceuil

        menuLayout = Nav.MenuLayout(screens_call)
        ecranLayout = QVBoxLayout()
        grid_layout = QGridLayout()

        first_graph = premierGraphique()
        second_graph = deuxiemeGraphique()
        third_graph  = troisiemeGraphique()
        fourth_graph = quatriemeGraphique()

        grid_layout.addWidget(first_graph,0,0)
        grid_layout.addWidget(second_graph,0,1)
        grid_layout.addLayout(third_graph.listlayout,1,0)
        grid_layout.addWidget(fourth_graph,1,1)
        

        # Créer un widget central et définir la grille comme layout
        ecranLayout.addLayout(menuLayout.menuLayout)
        ecranLayout.addLayout(grid_layout)

        self.setLayout(ecranLayout)
       
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
testeurs = [testeur for _ in range(4)]
            
def main():
    app = QApplication(sys.argv)
    fenetre = ScreenProfile(testeurs)
    fenetre.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    