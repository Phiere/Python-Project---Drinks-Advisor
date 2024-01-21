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

global data_base_choose
data_base_choose = 0

#Boutton permettant le choix de la database à utiliser
##BENE
class DataBaseChoice(QComboBox):
    def __init__(self,change_completion_lines):
        super().__init__()

        self.fonction = change_completion_lines

        self.addItem('Wines')
        self.addItem('Cocktails')
        self.addItem('Beers')
        self.addItem('Coffee')
        self.addItem('Mocktails')
        self.currentIndexChanged.connect(self.update)

    def update(self,index):
        global data_base_choose
        data_base_choose = index
        self.fonction()

#Créations des colonnes à compléter pour décrire la boisson sous forme d'une liste verticale 
##BENE
class ListeElementToComplete(QListWidget):
    def __init__(self)-> None:
        super().__init__()

        self.update()

    def update(self):
        self.clear()
        global data_base_choose
        names_columns = Db.choisir_db(data_base_choose,0).columns

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

##BENE
class CreationButton(QPushButton):
    def __init__(self)-> None:
        super().__init__()

        self.setText("Créer")
        self.clicked.connect(self.create_new_drink)

    def create_new_drink(self):
        global data_base_choose
        Cb.create_new_drink(Db.choisir_db(data_base_choose,0),self)

##Creation de l'écran
##BENE
class ScreenCreation(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Creation Window")
        self.resize(1000,500)

        data_base_choice = DataBaseChoice(self.update)
        self.list_element_to_complete = ListeElementToComplete()
        screen_layout = QVBoxLayout()
        creation_button = CreationButton()

        screen_layout.addWidget(data_base_choice)
        screen_layout.addWidget(self.list_element_to_complete)
        screen_layout.addWidget(creation_button)

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
    