# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:00:56 2024

@author: mariu
"""

import sys
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QLabel,QHBoxLayout,QWidget,QApplication,QVBoxLayout,QTextEdit,QPushButton

class LabelPrincipal(QLabel):
    def __init__(self, drink_name):
        super().__init__()
        self.setText(f'<font color="red"><b>Nom de la boisson : {drink_name}</b></font>')

class InformationsDisplay(QHBoxLayout):
    def __init__(self):
        super().__init__()
        description_text = QTextEdit()
        description_text.setPlaceholderText('Description de la boisson...')

        image_label = QLabel()
        image_label.setPixmap(QPixmap("codes/UI/Icones/boisson.jpg"))

        self.addWidget(description_text)
        self.addWidget(image_label)

class NotationsInteractions(QHBoxLayout):
    def __init__(self):
        super().__init__()
        add_favorite_button = QPushButton(' Ajouter en favori')
        add_favorite_button.setIcon(QIcon("codes/UI/Icones/favori.png"))
        
        comment_button = QPushButton(' Commenter')
        comment_button.setIcon(QIcon("codes/UI/Icones/comment.png"))
       
        rate_button = QPushButton(' Noter')
        rate_button.setIcon(QIcon("codes/UI/Icones/rate.png"))

        self.addWidget(add_favorite_button)
        self.addWidget(comment_button)
        self.addWidget(rate_button)

class Description(QWidget):
    def __init__(self, drink_name):
        super().__init__()
        self.setWindowTitle('Description de la Boisson')
        self.resize(1000,500)
      
        info_layout = QVBoxLayout()
        info_layout.addWidget(LabelPrincipal(drink_name))
        info_layout.addLayout(InformationsDisplay())
        info_layout.addLayout(NotationsInteractions())

        self.setLayout(info_layout)

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
    fenetre = Description("oui")
    fenetre.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    

"""
    # 1er layout - Barre de navigation
        home_button = QPushButton(self)
        home_button.setIcon(QIcon("codes/UI/Icones/home.png"))
        home_button.setFixedSize(QSize(30, 30))  # Ajustez la taille selon vos besoins      
        
        back_button = QPushButton(self)
        back_button.setIcon(QIcon("codes/UI/Icones/back.png"))
        back_button.setFixedSize(QSize(30, 30))  # Ajustez la taille selon vos besoins
        
        profile_button = QPushButton(self)
        profile_button.setIcon(QIcon("codes/UI/Icones/profile.png"))
        profile_button.setFixedSize(QSize(30, 30))  # Ajustez la taille selon vos besoins"""