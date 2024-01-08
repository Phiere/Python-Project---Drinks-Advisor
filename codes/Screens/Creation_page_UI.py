############################################################
############################################################
############################################################
# Description          
############################################################
############################################################
############################################################

from Importations import *
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
import Navigation as Nav
import Db_gestions as Db
import Creation_page_back as Cb

dbs = Db.choix_db('Wines')

#Boutton permettant le choix de la database à utiliser
class DropdownButtonWidget(QWidget):
    def __init__(self,change_completion_lines):
        super().__init__()

        self.fonction = change_completion_lines

        layout = QVBoxLayout(self)

        self.dropdown = QComboBox(self)
        self.dropdown .addItem('Wines')
        self.dropdown .addItem('Cocktails')
        self.dropdown .addItem('Beers')
        self.dropdown .addItem('Coffee')
        self.dropdown .addItem('Mocktails')

        # Connecter un signal pour détecter le changement de sélection
        self.dropdown .currentIndexChanged.connect(self.on_selection_changed)

        
    def on_selection_changed(self,index):
        selected_option = self.sender().itemText(index)
        self.fonction(Db.choix_db(selected_option)[0].columns)

#Créations des colonnes à compléter pour décrire la boisson sous forme d'une liste verticale 
class ListeElementToComplete(QWidget):
    def __init__(self,names_columns)-> None:
        super().__init__()

        self.listWidget = QListWidget()
        self.update(names_columns)

    def update(self,names_columns):
        self.listWidget.clear()
        for i in range(len(names_columns)):# Exemple avec 10 éléments
                listItem = QListWidgetItem(self.listWidget)
                listItem.setSizeHint(QSize(20,50))
                item = QLineEdit()
                item.setPlaceholderText(names_columns[i])
                self.listWidget.setItemWidget(listItem,item)

    def get_texts(self):
        # Récupérer le texte de chaque QLineEdit dans la QListWidget
        text_list = []
        for index in range(self.listWidget.count()):
            item = self.listWidget.item(index)
            widget = self.listWidget.itemWidget(item)
            if isinstance(widget, QLineEdit):
                text_list.append(widget.text())
        return text_list

##Creation de l'écran
class ScreenCreation(QWidget):
    def __init__(self,screens_call) -> None:
        super().__init__()
        self.setWindowTitle("Creation Window")
        self.resize(1000,500)


        menuLayout = Nav.MenuLayout(screens_call)
        
        self.adding_element_layout = QVBoxLayout()
        self.radio_button = DropdownButtonWidget(self.adding_lines_for_completion)
        self.adding_element_layout.addWidget(self.radio_button.dropdown)

        self.listWidget = ListeElementToComplete(dbs[0].columns)
        self.adding_element_layout.addWidget(self.listWidget.listWidget)
        self.adding_lines_for_completion(dbs[0].columns)

        launch_creation = QPushButton("Créer")
        launch_creation.pressed.connect(self.create_new_drink)
        self.adding_element_layout.addWidget(launch_creation)

        ecranLayout = QVBoxLayout()
        ecranLayout.addLayout(menuLayout.menuLayout)
        ecranLayout.addLayout(self.adding_element_layout)

        self.setLayout(ecranLayout)
    
    def adding_lines_for_completion(self,names_columns):
        self.listWidget.update(names_columns)
    
    def create_new_drink(self):
        Cb.create_new_drink(dbs[0],self.listWidget)

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
testeurs = [testeur,testeur,testeur,testeur]
            
def main():
    app = QApplication(sys.argv)
    fenetre = ScreenCreation(testeurs)
    fenetre.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    