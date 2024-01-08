# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:00:56 2024

@author: mariu
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Navigation as Nav

class Description(QWidget):
    def __init__(self, drink_name,screen_calls):
        super().__init__()

        # Initialisation de l'interface
        self.drink_name = drink_name
        self.init_ui(screen_calls)

    def init_ui(self,screen_calls):
        # 1er layout - Barre de navigation
        home_button = QPushButton(self)
        home_button.setIcon(QIcon("Icones/home.png"))
        home_button.setFixedSize(QSize(30, 30))  # Ajustez la taille selon vos besoins      
        
        back_button = QPushButton(self)
        back_button.setIcon(QIcon("Icones/back.png"))
        back_button.setFixedSize(QSize(30, 30))  # Ajustez la taille selon vos besoins
        
        profile_button = QPushButton(self)
        profile_button.setIcon(QIcon("Icones/profile.png"))
        profile_button.setFixedSize(QSize(30, 30))  # Ajustez la taille selon vos besoins
        
        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(home_button)
        navigation_layout.addWidget(back_button)
        navigation_layout.addStretch()  # Ajout d'un espace flexible
        navigation_layout.addWidget(profile_button)

        # 2ème layout - Description de la boisson
        name_label = QLabel(f'<font color="red"><b>Nom de la boisson : {self.drink_name}</b></font>')
        name_label.setAlignment(Qt.AlignCenter)  # Centre le texte
        description_text = QTextEdit()
        description_text.setPlaceholderText('Description de la boisson...')
        
        add_favorite_button = QPushButton(' Ajouter en favori')
        add_favorite_button.setIcon(QIcon("Icones/favori.png"))
        add_favorite_button.setFixedSize(QSize(550, 30))  # Ajustez la taille selon vos besoins
        
        comment_button = QPushButton(' Commenter')
        comment_button.setIcon(QIcon("Icones/comment.png"))
        comment_button.setFixedSize(QSize(550, 30))  # Ajustez la taille selon vos besoins 
       
        rate_button = QPushButton(' Noter')
        rate_button.setIcon(QIcon("Icones/rate.png"))
        rate_button.setFixedSize(QSize(550, 30))  # Ajustez la taille selon vos besoins 

        info_layout = QVBoxLayout()
        info_layout.addWidget(name_label)
        info_layout.addWidget(description_text)
        info_layout.addWidget(add_favorite_button)
        info_layout.addWidget(comment_button)
        info_layout.addWidget(rate_button)

        # 2ème layout à droite - Image de la boisson (à remplacer par le chemin de votre image)
        image_label = QLabel()
        image_label.setPixmap(QPixmap("Icones/boisson.jpg").scaled(250,800))
        image_layout = QVBoxLayout()
        image_layout.addWidget(image_label)
        
        # Layout principal pour les layouts d'info et d'image
        info_image_layout = QHBoxLayout()
        info_image_layout.addLayout(info_layout)
        info_image_layout.addLayout(image_layout)

        
        # Disposition principale
        main_layout = QVBoxLayout()
        main_layout.addLayout(navigation_layout)
        main_layout.addLayout(info_image_layout, 1)  # Ajout d'un facteur d'étirement
        
        # Assemblage final
        final_layout = QVBoxLayout()
        menuLayout = Nav.MenuLayout(screen_calls)
        final_layout.addLayout(menuLayout.menuLayout)
        final_layout.addLayout(main_layout)
        self.setLayout(final_layout)

        # Configurer la fenêtre
        self.setWindowTitle('Description de la Boisson')
        self.setGeometry(300, 300, 800, 600)

        # Afficher la fenêtre
        self.show()

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

testeurs = [testeur for _ in range(4)]
            


if __name__ == '__main__':
    app = QApplication([])
    window = Description('Nom de la Boisson Test',testeurs)
    app.exec_()