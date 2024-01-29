############################################################
############################################################
############################################################
# Description          
############################################################
############################################################
############################################################

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit,
                                    QComboBox,QListWidget,QListWidgetItem)
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize,QTimer

sys.path.append('codes/BackEnd/')
import Db_gestions as Db
import Creation_page_back as Cb
import Navigation as Nav




##BENE
class DataBaseChoice(QComboBox):
    def __init__(self,change_completion_lines):
        super().__init__()

        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.fonction = change_completion_lines

        self.addItem('Wines')
        self.addItem('Cocktails')
        self.addItem('Beers')
        self.addItem('Coffee')
        self.addItem('Mocktails')
        self.currentIndexChanged.connect(self.update)

    def update(self,index):
        Db.choix_de_la_data_base = index
        self.fonction()

#Créations des colonnes à compléter pour décrire la boisson sous forme d'une liste verticale 
##BENE
class ListeElementToComplete(QListWidget):
    def __init__(self)-> None:
        super().__init__()
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.update()

    def update(self):
        self.clear()
        names_columns = Db.dbsall[Db.choix_de_la_data_base ][0].columns

        for name in names_columns:
            if name not in ['Unnamed 0:','PersonalRating','Favorie'] :
                listItem = QListWidgetItem(self)
                listItem.setSizeHint(QSize(20,50))
                item = QLineEdit()
                item.setPlaceholderText(name)
                self.setItemWidget(listItem,item)

    def get_texts(self):
        # Récupérer le texte de chaque QLineEdit dans la QListWidget
        text_list = []
        for index in range(self.count()):
            item = self.item(index)
            widget = self.itemWidget(item)
            if isinstance(widget, QLineEdit):
                text_list.append(widget.text())
            widget.setText("")

        return text_list

##BENE
class CreationButton(QPushButton):
    def __init__(self,get_text,go_to_description)-> None:
        super().__init__()

        self.go_to_description = go_to_description
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.setText("Créer")
        self.function = get_text
        self.pressed.connect(self.on_pressed)
        self.released.connect(self.on_released)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)  
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.create_new_drink)

    def create_new_drink(self):
        Cb.create_new_drink(Db.choix_de_la_data_base,self.function)
        self.go_to_description()

    def on_pressed(self):
        self.timer.start()

    def on_released(self):
        if self.timer.isActive():
            self.timer.stop()

        

##Creation de l'écran
##BENE
class ScreenCreation(QWidget):
    def __init__(self,go_to_description) -> None:
        super().__init__()

        self.setStyleSheet("background-color: #1f1f1f")
        self.setWindowTitle("Creation Window")
        self.resize(1000,500)

        data_base_choice = DataBaseChoice(self.update)
        self.list_element_to_complete = ListeElementToComplete()
        get_text = self.list_element_to_complete.get_texts
        screen_layout = QVBoxLayout()
        creation_button = CreationButton(get_text,go_to_description=go_to_description)

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
    