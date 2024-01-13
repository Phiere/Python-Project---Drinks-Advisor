############################################################
############################################################
############################################################
# Description          
############################################################
############################################################
############################################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit,QComboBox,QListWidget,QListWidgetItem
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize 

import Navigation as Nav
sys.path.append('codes/BackEnd/')
import Db_gestions as Db
import Creation_page_back as Cb

dbs = Db.choix_db('Wines')

#Boutton permettant le choix de la database à utiliser
class DataBaseChoice(QComboBox):
    def __init__(self,change_completion_lines):
        super().__init__()

        self.fonction = change_completion_lines

        self.addItem('Wines')
        self.addItem('Cocktails')
        self.addItem('Beers')
        self.addItem('Coffee')
        self.addItem('Mocktails')

        # Connecter un signal pour détecter le changement de sélection
        self.currentIndexChanged.connect(self.on_selection_changed)

        
    def on_selection_changed(self,index):
        selected_option = self.itemText(index)
        self.fonction(Db.choix_db(selected_option)[0].columns)

#Créations des colonnes à compléter pour décrire la boisson sous forme d'une liste verticale 
class ListeElementToComplete(QListWidget):
    def __init__(self,names_columns)-> None:
        super().__init__()

        self.update(names_columns)

    def update(self,names_columns):
        self.clear()

        for i in range(1,len(names_columns)):
                
                listItem = QListWidgetItem(self)
                listItem.setSizeHint(QSize(20,50))
                item = QLineEdit()
                item.setPlaceholderText(names_columns[i])
                self.setItemWidget(listItem,item)

    def get_texts(self):
        # Récupérer le texte de chaque QLineEdit dans la QListWidget
        text_list = []
        for index in range(self.count()):
            item = self.item(index)
            widget = self.itemWidget(item)
            if isinstance(widget, QLineEdit):
                text_list.append(widget.text())
        return text_list


##Creation de l'écran
class ScreenCreation(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Creation Window")
        self.resize(1000,500)

        
        screen_layout = QVBoxLayout()
        screen_layout.addWidget(DataBaseChoice(self.adding_lines_for_completion))


        self.liste_element_to_complete = ListeElementToComplete(dbs[0].columns)
        screen_layout.addWidget(self.liste_element_to_complete)
        self.adding_lines_for_completion(dbs[0].columns)

        launch_creation = QPushButton("Créer")
        launch_creation.pressed.connect(self.create_new_drink)
        screen_layout.addWidget(launch_creation)


        self.setLayout(screen_layout)
    
    def adding_lines_for_completion(self,names_columns):
        self.liste_element_to_complete.update(names_columns)
    
    def create_new_drink(self):
        Cb.create_new_drink(dbs[0],self)

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
    