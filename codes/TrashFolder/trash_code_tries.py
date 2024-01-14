# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:00:56 2024

@author: mariu
"""

import sys
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QLabel,QHBoxLayout,QWidget,QApplication,QVBoxLayout,QTextEdit,QPushButton

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget, QApplication, QVBoxLayout, QTextEdit, QPushButton, \
    QMainWindow

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
        #image_label.setPixmap(QPixmap("codes/UI/Icones/boisson.jpg"))

        self.addWidget(description_text)
        self.addWidget(image_label)

class FavoriteInteraction(QPushButton):
    def __init__(self):
        super().__init__()

        self.star_icon = QIcon("codes/UI/Icones/star_empty.png")
        self.setText('Ajouter en Favori')
        self.setIcon(QIcon(self.star_icon))
        self.clicked.connect(self.update_status)
        self.is_favorite = 0 ##for the moment, modify to the actual status after

    def update_status(self):
        filled_star_icon = QIcon("codes/UI/Icones/star_filled.png")

        self.is_favorite = not self.is_favorite
        if self.is_favorite:
            self.setIcon(filled_star_icon)
        else:
            self.setIcon(self.star_icon)

class CommentInteracton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText('Commenter')
        self.setIcon(QIcon("codes/UI/Icones/comment.png"))
        self.clicked.connect(self.update)

    def update(self):
        pass

#Revoir ça, j'aime pas
class RatingInteraction(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText(' Noter')
        self.setIcon(QIcon("codes/UI/Icones/rate.png"))
        self.clicked.connect(self.open_rating_page)

    def open_rating_page(self):
        rating_page = DrinkRatingPage('oui', QSize(100,100))
        rating_page.show()

class DrinkRatingPage(QWidget):
    def __init__(self, drink_name, parent_size):
        super().__init__()
        self.drink_name = drink_name
        self.setWindowTitle("Noter la boisson")

        # Rendre la fenêtre transparente
        self.setWindowOpacity(0.95)

        self.setGeometry(200, 200, parent_size.width(), parent_size.height())  # Utiliser la taille du parent
        self.setStyleSheet("background-color: rgba(51, 51, 51, 0.8);")

        label1 = QLabel(self)
        label1.setText("Vous avez goûté cette boisson ?")
        label1.setStyleSheet("color: white; font-size: 12pt; background-color: rgba(41, 41, 41, 1);")
        label1.setAlignment(Qt.AlignCenter)
        label1.setGeometry(0, int(parent_size.height() * 0.2), self.width(), 30)

        label2 = QLabel(self)
        label2.setText("Sélectionnez la note que vous souhaitez lui donner avec les étoiles ci-dessous !")
        label2.setStyleSheet("color: white; font-size: 12pt; background-color: rgba(41, 41, 41, 1);")
        label2.setAlignment(Qt.AlignCenter)
        label2.setGeometry(0, int(parent_size.height() * 0.3), self.width(), 30)
        
        stars_frame = QWidget(self)
        stars_frame.setGeometry(int((self.width() - 200) / 2), int(parent_size.height() * 0.4), 200, 50)

        self.stars_images = []
        for i in range(1, 6):
            empty_star = QPixmap("codes/UI/Icones/star_empty.png").scaled(40, 40)
            filled_star = QPixmap("codes/UI/Icones/star_filled.png").scaled(40, 40)
            self.stars_images.append((empty_star, filled_star))

        self.rating = 0

        self.star_buttons = []
        for i in range(5):
            star_button = QPushButton(stars_frame)
            star_button.setIcon(QIcon(self.stars_images[i][0]))
            star_button.setGeometry(40 * i, 0, 40, 50)
            star_button.clicked.connect(lambda _, idx=i + 1: self.on_star_click(idx))
            star_button.installEventFilter(self)
            self.star_buttons.append(star_button)

        validate_button = QPushButton(self)
        validate_button.setText("Valider")
        validate_button.clicked.connect(self.write_to_database)
        validate_button.setGeometry(int((self.width() - 100) / 2), int(parent_size.height() * 0.6), 100, 30)

    def on_star_click(self, index):
        if index > self.rating:
            # Si l'utilisateur clique sur une étoile inférieure à celle qui était précédemment sélectionnée
            for i in range(index):
                self.star_buttons[i].setIcon(QIcon(self.stars_images[i][1]))
        else:
            # Si l'utilisateur clique sur une étoile égale ou supérieure à celle qui était précédemment sélectionnée
            for i in range(index, 5):
                self.star_buttons[i].setIcon(QIcon(self.stars_images[i][0]))
        
        self.rating = index

    def eventFilter(self, obj, event):
        if obj in self.star_buttons:
            index = self.star_buttons.index(obj) + 1
            if event.type() == event.Enter:
                for i in range(index):
                    self.star_buttons[i].setIcon(QIcon(self.stars_images[i][1]))
            elif event.type() == event.Leave:
                if self.rating == 0:
                    for i in range(5):
                        self.star_buttons[i].setIcon(QIcon(self.stars_images[i][0]))
                else:
                    for i in range(self.rating, 5):
                        self.star_buttons[i].setIcon(QIcon(self.stars_images[i][0]))
        return super().eventFilter(obj, event)

    def write_to_database(self):
        print(f"Note pour {self.drink_name}: {self.rating}/5")
        self.close()


class NotationsInteractions(QHBoxLayout):
    def __init__(self, parent, drink_name):
        super().__init__()
        self.parent = parent
        self.drink_name = drink_name

        self.addWidget(FavoriteInteraction())
        self.addWidget(CommentInteracton())
        self.addWidget(RatingInteraction())



class Description(QMainWindow):
    def __init__(self, drink_name):
        super().__init__()
        self.setWindowTitle('Description de la Boisson')
        self.resize(1000, 500)

        info_layout = QVBoxLayout()
        info_layout.addWidget(LabelPrincipal(drink_name))
        info_layout.addLayout(InformationsDisplay())
        info_layout.addLayout(NotationsInteractions(self, drink_name))

        central_widget = QWidget()
        central_widget.setLayout(info_layout)
        self.setCentralWidget(central_widget)


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