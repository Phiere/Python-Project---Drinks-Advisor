 # -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:00:56 2024

@author: mariu
"""

import sys
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QLabel,QHBoxLayout,QWidget,QApplication,QVBoxLayout,QScrollArea,QPushButton,QLineEdit
from PyQt5.QtCore import QSize,Qt
import Research_page_UI as RU

sys.path.append('codes/BackEnd/')
import Db_gestions as Db
import pandas as pd
import Description_page_back as Dp

class LabelPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: #1f1f1f;")

        self.drink_name = QLabel()
        self.drink_name.setWordWrap(True)  # Pour que le texte s'ajuste automatiquement à la largeur du QLabel
        self.drink_name.setTextInteractionFlags(Qt.TextSelectableByMouse)  # Rend le texte sélectionnable par la souris
        self.drink_name.setFixedHeight(40)
        layout = QHBoxLayout(self)  # Ajouter un QHBoxLayout au widget
        layout.addWidget(self.drink_name)

    def update(self):
        drink_name = Dp.get_name_from_drink()
        self.drink_name.setText(f'<font color="red"><b>Boisson : {drink_name}</b></font>')


class InformationsDisplay(QScrollArea):
    def __init__(self):
        super().__init__()

        self.scroll_content = QWidget()
        layout = QVBoxLayout(self.scroll_content)
        layout.setAlignment(Qt.AlignTop)

        self.description_text = QLabel()
        self.description_text.setWordWrap(True)
        self.description_text.setTextInteractionFlags(Qt.TextSelectableByMouse)

        layout.addWidget(self.description_text)
        self.setWidgetResizable(True)
        self.setWidget(self.scroll_content)

    def update(self):
        texte =  Dp.get_description_from_drink()
        self.description_text.setText(texte)

        


class FavoriteInteraction(QPushButton):
    def __init__(self):
        super().__init__()

        self.star_icon_empty = QIcon("codes/UI/Icones/star_empty.png")
        self.star_icon_filled = QIcon("codes/UI/Icones/star_filled.png")

        self.setText('Ajouter en Favori')
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.setFixedHeight(40)
        self.clicked.connect(self.update_status)
        self.setIcon(self.star_icon_empty)

    def update_icon(self):
        if Dp.get_status_favori(): self.setIcon(self.star_icon_filled)
        else: self.setIcon(self.star_icon_empty)

    def update_status(self):
        Dp.update_status_favori()
        self.update_icon()
        


class CommentInteracton(QHBoxLayout):
    def __init__(self):
        super().__init__()

        bouton = QPushButton('Commenter')
        bouton.setIcon(QIcon("codes/UI/Icones/comment.png"))
        bouton.setStyleSheet("background-color: #404040; color: #ffffff;")
        bouton.clicked.connect(self.comment)
        bouton.setFixedSize(150,40)

        self.texte = QLineEdit()
        self.texte.setFixedHeight(40)
        self.setStretchFactor(self.texte, 6)
        
        self.addWidget(bouton)
        self.addWidget(self.texte)


    def update(self):
        self.texte.setText('')
        commentaire =  Dp.get_comment()
        self.texte.setPlaceholderText(commentaire)
    
    def comment(self):
        Dp.update_comment(self.texte.text())



class RatingInteraction(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.prec_rating = 0
        self.new_rating = 0 
        self.stars_images = []
        for i in range(1, 6):
            empty_star = QPixmap("codes/UI/Icones/star_empty.png").scaled(40, 40)
            filled_star = QPixmap("codes/UI/Icones/star_filled.png").scaled(40, 40)
            self.stars_images.append((empty_star, filled_star))

        self.star_buttons = []
        for i in range(5):
            star_button = QPushButton()
            star_button.setIcon(QIcon(self.stars_images[i][0]))
            star_button.setFixedSize(80, 40)
            star_button.clicked.connect(lambda _, idx=i + 1: self.update_status(idx))
            star_button.installEventFilter(self)
            self.star_buttons.append(star_button)

            # Ajoute chaque étoile au layout horizontal
            self.addWidget(star_button)

    def on_star_click(self, index):
        if self.new_rating > self.prec_rating:
            for i in range(index):
                self.star_buttons[i].setIcon(QIcon(self.stars_images[i][1]))
        else:
            for i in range(index, 5):
                self.star_buttons[i].setIcon(QIcon(self.stars_images[i][0]))
        
        self.prec_rating = index
    
    def eventFilter(self, obj, event):
        if obj in self.star_buttons:
            index = self.star_buttons.index(obj) + 1
            if event.type() == event.Enter:
                for i in range(index):
                    self.star_buttons[i].setIcon(QIcon(self.stars_images[i][1]))
            elif event.type() == event.Leave:
                if self.prec_rating == 0:
                    for i in range(5):
                        self.star_buttons[i].setIcon(QIcon(self.stars_images[i][0]))
                else:
                    for i in range(self.prec_rating, 5):
                        self.star_buttons[i].setIcon(QIcon(self.stars_images[i][0]))
        return super().eventFilter(obj, event)
    
    def update_icon(self):
        rating = Dp.get_rating()
        self.on_star_click(int(rating))

    def update_status(self,idx):
        self.new_rating = idx
        Dp.update_rating(self.new_rating)
        self.update_icon()
    
    
class NotationsInteractions(QVBoxLayout):
    def __init__(self, ):
        super().__init__()

        self.favorite_interaction = FavoriteInteraction()
        self.rating_interaction = RatingInteraction()
        self.comment_interaction = CommentInteracton()


        self.addWidget(self.favorite_interaction)
        self.addLayout(self.rating_interaction)
        self.addLayout(self.comment_interaction)

    def update(self):
        self.favorite_interaction.update_icon()
        self.rating_interaction.update_icon()
        self.comment_interaction.update()
        

##BENE
class Description(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #1f1f1f; color: #ffffff;")
        self.setWindowTitle('Description de la Boisson')
        self.setGeometry(200,200,1000,500)


        self.drink_name = LabelPrincipal()
        self.informations_display = InformationsDisplay()
        self.notations_interactions = NotationsInteractions()
        info_layout = QVBoxLayout()
  
        info_layout.addWidget(self.drink_name)
        info_layout.addWidget(self.informations_display)
        info_layout.setStretchFactor(self.informations_display,3)
        info_layout.addLayout(self.notations_interactions)

        self.setLayout(info_layout)
    
    def update(self):
        self.drink_name.update()
        self.informations_display.update()
        self.notations_interactions.update()

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
    fenetre = Description()
    fenetre.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
