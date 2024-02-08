############################################################
############################################################
############################################################
#    
############################################################
############################################################
############################################################

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit,
                                    QListWidget,QListWidgetItem, QPushButton,QLabel,
                                    QTextEdit, QGraphicsView, QGraphicsPixmapItem, QGraphicsEllipseItem)
from PyQt5.QtCore import QSize

sys.path.append('codes/BackEnd/')
import Db_gestions as Db
import Edit_page_back as Eb
import Navigation as Nav


#Créations des colonnes à compléter pour décrire la boisson sous forme d'une liste verticale 
class  Carremodif(QWidget):
    def __init__(self,name,colonne)-> None:
        super().__init__()
        box_layout = QHBoxLayout()
        self.contenu = QTextEdit()
        self.contenu.setText(str(name))
        colonne_name = QLabel(colonne)
        box_layout.addWidget(colonne_name)
        box_layout.addWidget(self.contenu)
        self.setLayout(box_layout)

    
class ListeElementToComplete(QListWidget):
    
    def __init__(self)-> None:
        super().__init__()
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.names = []
        self.update()

    def update(self):
        self.clear()
        data_base = Db.dbsall[Db.choix_de_la_data_base ][0]
        names_columns = data_base.columns
        index_boisson = Db.index_boisson
        self.names = []
        for name in names_columns:
            if name not in ['PersonalRating', 'Comment', 'Favorite'] :
                self.names.append(name)
                itemtexte = data_base.at[index_boisson,name]
                listItem = QListWidgetItem(self)
                listItem.setSizeHint(QSize(20,50))
                item = Carremodif(str(itemtexte),name)
                self.setItemWidget(listItem,item)

    def get_texts(self):
        # Récupérer le texte de chaque QTextEdit dans la QListWidget
        text_list = []
        name_list = []

        for index in range(self.count()):
            item = self.item(index)
            widget = self.itemWidget(item)
            
            if isinstance(widget, Carremodif):  # Vérifier si le widget est une instance de Carremodif
                texte = widget.contenu.toPlainText()  # Utiliser toPlainText() pour QTextEdit
                name = widget.contenu.objectName()  # Assumer que vous avez défini un objectName pour QTextEdit, sinon utiliser une autre méthode pour identifier

                text_list.append(texte)
                name_list.append(name)

        return text_list, self.names
    
    def reset_fields(self):
        for index in range(self.count()):
            item = self.item(index)
            widget = self.itemWidget(item)
            if isinstance(widget, QLineEdit):
                widget.clear()



class CreationButton(QPushButton):
    def __init__(self, get_text, go_to_description, list_element_to_complete):
        super().__init__()

        self.go_to_description = go_to_description
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.setText("Edit")
        self.function = get_text
        self.clicked.connect(self.create_new_drink)
        self.list_element_to_complete = list_element_to_complete


    def create_new_drink(self):
        Eb.create_new_drink(self.function)
        self.go_to_description()



class ScreenCreation(QWidget):
    """Création de l'écran regroupant le choix de la database, les éléments à compléter et ceux de notations
    
    - go_to_description : fonction permettant de renvoyer à l'écran de description pour la boisson choisie
    - update : met à jour les champs de création en fonction de la data base choisie"""
    def __init__(self, go_to_description) -> None:
        super().__init__()

        self.setStyleSheet("background-color: #1f1f1f")
        self.setWindowTitle("Creation Window")
        self.resize(1000, 500)

         # Créer d'autres éléments de votre interface
        self.list_element_to_complete = ListeElementToComplete()

        # Créer l'animation widget et le bouton associé

        get_text = self.list_element_to_complete.get_texts
        creation_button = CreationButton(get_text, go_to_description=go_to_description, list_element_to_complete = self.list_element_to_complete)
        creation_button.setFixedHeight(40)

        # Création du QHBoxLayout du bouton et de l'animation
        animation_layout = QHBoxLayout()
        animation_layout.addStretch(3)
        animation_layout.addWidget(creation_button)
        animation_layout.addStretch(3)

        # Mise en place de la disposition verticale
        screen_layout = QVBoxLayout()
        screen_layout.addWidget(self.list_element_to_complete)
        screen_layout.addLayout(animation_layout)

        self.update()
        self.setLayout(screen_layout)

    def update(self):
        self.list_element_to_complete.update()
    

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
    fenetre = ScreenCreation()
    fenetre.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    