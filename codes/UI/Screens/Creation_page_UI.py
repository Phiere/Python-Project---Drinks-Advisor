############################################################
############################################################
############################################################
# Description          
############################################################
############################################################
############################################################

import sys
import time
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit,
                                    QComboBox,QListWidget,QListWidgetItem, QPushButton,
                                    QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QGraphicsEllipseItem)
from PyQt5.QtCore import QSize,QTimer, Qt
from PyQt5.QtGui import QPixmap

sys.path.append('codes/BackEnd/')
import Db_gestions as Db
import Creation_page_back as Cb
import Navigation as Nav


##BENE
class DataBaseChoice(QComboBox):
    def __init__(self,change_completion_lines):
        super().__init__()

        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.setFixedHeight(40)

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
class CircleAnimationWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent  # Référence à l'objet parent = ScreenCreation
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
    def __init__(self, get_text, go_to_description, animation_widget):
        super().__init__()

        self.go_to_description = go_to_description
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.setText("Créer")
        self.function = get_text
        self.pressed.connect(self.on_pressed)
        self.released.connect(self.on_released)

        self.animation_widget = animation_widget

    def create_new_drink(self):
        Cb.create_new_drink(Db.choix_de_la_data_base, self.function)
        self.go_to_description()

    def on_pressed(self):
        self.animation_widget.startAnimation()

    def on_released(self):
        if self.animation_widget.timer.isActive():
            self.animation_widget.timer.stop()
        else:
            self.create_new_drink()
            self.animation_widget.pixmap_item.setPixmap(QPixmap())

##Creation de l'écran
##BENE
class ScreenCreation(QWidget):
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
        creation_button = CreationButton(get_text, go_to_description=go_to_description, animation_widget=self.animation_widget)
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
        #screen_layout.addWidget(creation_button)
        #screen_layout.addWidget(self.animation_widget)  # Ajouter le widget d'animation à la disposition

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
    