############################################################
############################################################
############################################################
#Construction de la page correspondant au profil de l'utilisateur. 
############################################################
############################################################
############################################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QFrame,QGridLayout,QHBoxLayout,QLabel,QListWidgetItem,QListWidget
from PyQt5.QtCore import QSize
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

sys.path.append('codes/BackEnd/')
import Profil_page_back as Pb

categories = ['Vins', 'Cocktails', 'Cafés', 'Mocktails', 'Bières']

class FavorieDataLine(QWidget):
    def __init__(self,textes_a_afficher):
        super().__init__()

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

        favories_dfs = Pb.favoris_extraction()
        categories = ['Vins', 'Cocktails', 'Cafés', 'Mocktails', 'Bières']

        for j in range(len(favories_dfs)) :
            favorie_df = favories_dfs[j]
            for i in range(len(favorie_df)):

                listItem = QListWidgetItem(self)
                ligne = favorie_df.iloc[i]
                element_ligne = [str(e) for e in ligne]
                element_ligne.append(categories[j])
                print(element_ligne)
                favorie_data_line = FavorieDataLine(element_ligne)
                listItem.setSizeHint(favorie_data_line.sizeHint())
                self.addItem(listItem)
                self.setItemWidget(listItem, favorie_data_line)

class MeanByCategories(QWidget):
    def __init__(self):     
        super().__init__()

        # Créer un canevas pour le graphique
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout = QGridLayout(self)
        layout.addWidget(self.canvas)

        # Générer des données pour l'exemple
        values = Pb.notes_mean()
        print(values)
        # Tracer l'histogramme
        self.ax.bar(categories, values, color='skyblue')
        #self.ax.set_title('Exemple d\'histogramme')
        #self.ax.set_xlabel('Catégories')
        #self.ax.set_ylabel('Valeurs')

        # Mettre à jour le canevas
        self.canvas.draw()

class FavoriesByCategories(QWidget):
    def __init__(self):
        super().__init__()

        # Créer un canevas pour le graphique
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout = QGridLayout(self)
        layout.addWidget(self.canvas)

        # Générer des données pour l'exemple
        values = Pb.favories_count()

        # Tracer l'histogramme
        self.ax.bar(categories, values, color='skyblue')
        #self.ax.set_title('Exemple d\'histogramme')
        #self.ax.set_xlabel('Catégories')
        #self.ax.set_ylabel('Valeurs')

        # Mettre à jour le canevas
        self.canvas.draw()

##Creation de l'écran
class ScreenProfile(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Profil Window")
        self.resize(1000,500)

        ##Partie droite avec les graphiques
        graphiques_layout = QVBoxLayout()
        graphiques_layout.addWidget( MeanByCategories() )
        graphiques_layout.addWidget(FavoriesByCategories())

        ##
        favorie_data_diplay = FavorieDataDisplay()

        ##
        ecran_layout = QHBoxLayout()
        ecran_layout.addWidget(favorie_data_diplay,5)
        ecran_layout.addLayout(graphiques_layout,5)

        self.setLayout(ecran_layout)
       
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
    