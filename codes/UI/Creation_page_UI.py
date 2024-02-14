############################################################
############################################################
############################################################
#Script Partie Graphique Page Création. Créer l'écran création qui permet
#d'ajouter de nouvelles boissons aux data_frames existants.       
############################################################
############################################################
############################################################

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit,
                                    QComboBox,QListWidget,QListWidgetItem, QPushButton,QMessageBox,
                                    QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QGraphicsEllipseItem)
from PyQt5.QtCore import QSize,QTimer, Qt
from PyQt5.QtGui import QPixmap

sys.path.append('codes/BackEnd/')
import Db_gestions as Db
import Creation_page_back as Cb


class DataBaseChoice(QComboBox):
    """Combo box permettant de choisir la base de données sur laquelle se fera la création.
    
    - change_completion_lines : fonction appelant au rafraichissement de l'écran pour adapter les QLineEdit à la database
    - update : change la database et l'écran en fonction de l'item choisi"""
    def __init__(self,change_completion_lines):
        super().__init__()
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.setFixedHeight(40)

        self.fonction = change_completion_lines

        self.addItem('Wines')
        self.addItem('Cocktails')
        self.addItem('Beers')
        self.addItem('Coffees')
        self.addItem('Mocktails')
        self.currentIndexChanged.connect(self.update)

    def update(self,index):
        Db.choix_de_la_data_base = index
        self.fonction()


class ListeElementToComplete(QListWidget):
    """Créations des colonnes à compléter pour décrire la boisson sous forme d'une liste verticale 
    
    - update : met à jour la liste des LineEdit en fonction de la base de données choisie
    - get_texts : récupère la liste des textes rentrés dans les LinesEdit et vérifie que leur format correspond à la colonne choisie
    """
    def __init__(self)-> None:
        super().__init__()
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.update()

    def update(self):
        self.clear()
        names_columns = Db.dbsall[Db.choix_de_la_data_base ][0].columns
        for name in names_columns:
            if name not in ['PersonalRating', 'Comment', 'Favorite'] :
                listItem = QListWidgetItem(self)
                listItem.setSizeHint(QSize(20,50))
                item = QLineEdit()
                if name in Db.list_elements :
                    item.setPlaceholderText(name+" if more than 1 split with ',' ")
                else :
                    item.setPlaceholderText(name)
                self.setItemWidget(listItem,item)

    def get_texts(self):
        # Récupérer le texte de chaque QLineEdit dans la QListWidget
        text_list = []
        name_list = []
        number_elements = Db.number_elements

        for index in range(self.count()):
            item = self.item(index)
            widget = self.itemWidget(item)
            
            if isinstance(widget, QLineEdit):
                texte = widget.text()
                name = widget.placeholderText()
                name.replace(" if more than 1 split with ',' ",'')
                if texte:
                    if name in number_elements:
                        if not texte.isdigit():
                            texte = 'numberFalse'
                    else:
                        if texte.isdigit():
                            texte = 'strFalse'

                text_list.append(texte)
                name_list.append(name)
        for i in range(len(name_list)):
            name_list[i] = name_list[i].replace(" if more than 1 split with ',' ",'')
        return text_list,name_list
    
    def reset_fields(self):
        for index in range(self.count()):
            item = self.item(index)
            widget = self.itemWidget(item)
            if isinstance(widget, QLineEdit):
                widget.clear()
    

class CircleAnimationWidget(QWidget):
    """Animation de chargement pour le bouton création
    
    - updateAnimation : met à jour l'animation
    - start animation : démarre l'animation"""
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent; border: none;")

        self.circle_item = QGraphicsEllipseItem(0, 0, 0, 0)
        pen = self.circle_item.pen()
        pen.setColor(Qt.white)
        self.circle_item.setPen(pen)

        self.pixmap_item = QGraphicsPixmapItem()

        self.scene = QGraphicsScene(self)
        self.scene.addItem(self.circle_item)
        self.scene.addItem(self.pixmap_item)

        self.view = QGraphicsView(self.scene)
        layout = QVBoxLayout(self)
        layout.addWidget(self.view)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateAnimation)

    def updateAnimation(self):
        progress = self.animation_step / self.animation_steps

        # Calculer la nouvelle taille du cercle pour atteindre un diamètre de 35
        new_size = 35 * progress
        self.circle_item.setRect(0, 0, new_size, new_size)

        if progress >= 1.0:
            self.circle_item.setRect(0, 0, 0, 0)
            pixmap = QPixmap("codes/UI/Icones/valide.png").scaled(40, 40, Qt.KeepAspectRatio)
            self.pixmap_item.setPixmap(pixmap)

        if self.animation_step < self.animation_steps:
            self.animation_step += 1
        else:
            self.timer.stop()

    def startAnimation(self):
        self.animation_duration = 1000
        self.animation_step = 0
        self.animation_steps = int(self.animation_duration / 100)
        self.timer.start(100)


class CreationButton(QPushButton):
    """Ajout du bouton Création ("Add") permettant l'ajout d'une boisson dans un dataframe existant
    
    - create_new_drink : fonction permettant d'écrire les éléments récupérés dans chacun des champs de la page création dans le dataframe choisi
    - on_pressed : vérifie le format de remplissage des champs et lance l'animation de validation si pas d'erreur
    - on_released : arrête l'animation si le bouton n'a pas été appuyé assez longtemps et crée la nouvelle boisson sinon"""
    def __init__(self, get_text, go_to_description, list_element_to_complete, animation_widget):
        super().__init__()

        self.go_to_description = go_to_description
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.setText("Add")
        self.function = get_text
        self.pressed.connect(self.on_pressed)
        self.released.connect(self.on_released)
        self.list_element_to_complete = list_element_to_complete
        self.animation_widget = animation_widget

    def create_new_drink(self):
        recovered_text,recovered_names = self.function()
        Cb.create_new_drink(recovered_text,recovered_names)
        self.go_to_description()
        self.list_element_to_complete.reset_fields()

    def on_pressed(self):
        recovered_text,recovered_names = self.function()
        is_error,invalid_indices = Cb.texte_vides(recovered_text)
        if not(is_error):
            self.animation_widget.startAnimation()
            for index in range(self.list_element_to_complete.count()):
                item = self.list_element_to_complete.item(index)
                if item:
                    widget = self.list_element_to_complete.itemWidget(item)
                    if isinstance(widget, QLineEdit):
                        widget.setStyleSheet("background-color: #404040;")
        elif is_error == 'strFalse':
            for index in invalid_indices:
                item = self.list_element_to_complete.item(index)
                if item:
                    widget = self.list_element_to_complete.itemWidget(item)
                    if isinstance(widget, QLineEdit):
                        widget.setStyleSheet("background-color: orange;")
            msg_box = QMessageBox()
            msg_box.setStyleSheet("background-color: #404040; color: #ffffff;")
            msg_box.setWindowTitle("Warning")
            msg_box.setText("Please fill in the orange fields with words")
            msg_box.exec_()
        elif is_error == 'numberFalse':
            for index in invalid_indices:
                item = self.list_element_to_complete.item(index)
                if item:
                    widget = self.list_element_to_complete.itemWidget(item)
                    if isinstance(widget, QLineEdit):
                        widget.setStyleSheet("background-color: red;")
            msg_box = QMessageBox()
            msg_box.setStyleSheet("background-color: #404040; color: #ffffff;")
            msg_box.setWindowTitle("Warning")
            msg_box.setText("Please fill in the red fields with numbers")
            msg_box.exec_()
        else:
            msg_box = QMessageBox()
            msg_box.setStyleSheet("background-color: #404040; color: #ffffff;")
            msg_box.setWindowTitle("Warning")
            msg_box.setText("Please fill in at least one field to create a new drink")
            msg_box.exec_()

    def on_released(self):
        recovered_text,_ = self.function()
        is_error,invalid_indices = Cb.texte_vides(recovered_text)
        if not(is_error):
            if self.animation_widget.timer.isActive():
                self.animation_widget.timer.stop()
                self.animation_widget.circle_item.setRect(0, 0, 0, 0)
                msg_box = QMessageBox()
                msg_box.setStyleSheet("background-color: #404040; color: #ffffff;")
                msg_box.setWindowTitle("Warning")
                msg_box.setText("Please keep the button pressed for at least 2 seconds to create a new drink")
                msg_box.exec_()
            else:
                self.create_new_drink()
                self.animation_widget.pixmap_item.setPixmap(QPixmap())


class ScreenCreation(QWidget):
    """Création de l'écran regroupant le choix de la database, les éléments à compléter et ceux de notation
    
    - go_to_description : fonction permettant de renvoyer à l'écran de description pour la boisson choisie
    - update : met à jour les champs de création en fonction de la data base choisie"""
    def __init__(self, go_to_description) -> None:
        super().__init__()

        self.setStyleSheet("background-color: #1f1f1f")
        self.setWindowTitle("Creation Window")
        self.resize(1000, 500)

         # Créer d'autres éléments de votre interface
        data_base_choice = DataBaseChoice(self.update)
        self.list_element_to_complete = ListeElementToComplete()

        # Créer l'animation widget et le bouton associé
        self.animation_widget = CircleAnimationWidget(self)
        self.animation_widget.setFixedHeight(100)
        get_text = self.list_element_to_complete.get_texts
        creation_button = CreationButton(get_text, go_to_description=go_to_description, list_element_to_complete = self.list_element_to_complete, animation_widget=self.animation_widget)
        creation_button.setFixedHeight(40)

        # Création du QHBoxLayout du bouton et de l'animation
        animation_layout = QHBoxLayout()
        animation_layout.addStretch(3)
        animation_layout.addWidget(creation_button)
        animation_layout.addWidget(self.animation_widget)
        animation_layout.addStretch(3)

        # Mise en place de la disposition verticale
        screen_layout = QVBoxLayout()
        screen_layout.addWidget(data_base_choice)
        screen_layout.addWidget(self.list_element_to_complete)
        screen_layout.addLayout(animation_layout)

        self.update()
        self.setLayout(screen_layout)

    def update(self):
        self.list_element_to_complete.update()
    

############################################################
############################################################
############################################################
# Test : Les test pour l'interface utilisateur se feront en constatant
        #visuellement si les actions sont effectuées. Les test suivants doivent 
        #être réalisés.
# - 1 : La comboBox permet de choisir la data_base à remplir
# - 2 : Les lignes de remplissage correspondent aux colonnes de la database choisie
# - 3 : Il est possible de remplir les lignes de création
# - 4 : Le bouton add lance effectue les actions suivantes :
        # 4.1 : si rien n'est rempli, la fenêtre affiche un warning
        # 4.2 : si un champs est mal rempli, la fenetre affiche un warning et colorie la case correspondate
        # 4.3 : si pas de problème; le bouton demande un appui prolongé pour la création d'une boisson  
        # 4.4 : lors d'un appui prolongé, une animation de validation se lance       
############################################################
############################################################
############################################################
                
def display_test():
    """Fonction de test d'affichage de l'écran création"""
    app = QApplication(sys.argv)
    fenetre = ScreenCreation(lambda : 1)
    fenetre.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test = input("Tester les fonctions du script ? (0/1) : ")
    if test : display_test()
    
    