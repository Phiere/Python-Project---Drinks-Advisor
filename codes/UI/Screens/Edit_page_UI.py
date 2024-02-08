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
                                    QTextEdit)
from PyQt5.QtCore import QSize

sys.path.append('codes/BackEnd/')
import Db_gestions as Db
import Edit_page_back as Eb



#V0.1
class  ModificationLayout(QWidget):
    """Layout contenant la ligne à modifiée ainsi que son titre afin de se reprérer.
    
    - name : texte de description correspondant au titre
    - colonne : nom de la colonne associée à la description"""
    def __init__(self,name,colonne)-> None:
        super().__init__()
        box_layout = QHBoxLayout()
        self.contenu = QTextEdit()
        self.contenu.setText(str(name))
        colonne_name = QLabel(colonne)

        box_layout.addWidget(colonne_name)
        box_layout.addWidget(self.contenu)
        self.setLayout(box_layout)

#V0.0
class ListeElementToComplete(QListWidget):
    """Assemblage des lignes de modification"""
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
                item = ModificationLayout(str(itemtexte),name)
                self.setItemWidget(listItem,item)

    def get_texts(self):
        text_list = []

        for index in range(self.count()):
            item = self.item(index)
            widget = self.itemWidget(item)
            
            if isinstance(widget, ModificationLayout): 
                texte = widget.contenu.toPlainText()  
                text_list.append(texte)
  
        return text_list, self.names
    
#V0.1
class EditButton(QPushButton):
    """Effectue la modification de la data base et retourne à descritpion
    
    - get_text : fonction de récupération des textes rentrés en QTextEdit
    - go_to_description : fonction d'appel à l'écran description"""
    def __init__(self, get_text, go_to_description):
        super().__init__()

        self.go_to_description = go_to_description
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.setText("Edit")
        self.function = get_text
        self.clicked.connect(self.create_new_drink)



    def create_new_drink(self):
        Eb.create_new_drink(self.function)
        self.go_to_description()

#V0.1
class ScreenEdition(QWidget):
    """Création de l'écran regroupant les éléments à compléter pour modifier la databse
    
    - go_to_description : fonction permettant de renvoyer à l'écran de description pour la boisson choisie
    - update : met à jour les champs de création en fonction de la boisson choisie"""
    def __init__(self, go_to_description) -> None:
        super().__init__()

        self.setStyleSheet("background-color: #1f1f1f")
        self.setWindowTitle("Creation Window")
        self.resize(1000, 500)

         # Créer d'autres éléments de votre interface
        self.list_element_to_complete = ListeElementToComplete()

        # Créer l'animation widget et le bouton associé

        get_text = self.list_element_to_complete.get_texts
        creation_button = EditButton(get_text, go_to_description=go_to_description)
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
    fenetre = ScreenEdition()
    fenetre.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    