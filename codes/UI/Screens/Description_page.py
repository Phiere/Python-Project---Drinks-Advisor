 # -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:00:56 2024

@author: mariu
"""

import sys
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QLabel,QHBoxLayout,QWidget,QApplication,QVBoxLayout,QTextEdit,QPushButton,QLineEdit
from PyQt5.QtCore import QSize,Qt
import Research_page_UI as RU
import ast
sys.path.append('codes/BackEnd/')
import Db_gestions as Db
import Research_page_back as RB 
import pandas as pd

class LabelPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: #1f1f1f;")

        self.drink_name = QLabel()
        self.drink_name.setWordWrap(True)  # Pour que le texte s'ajuste automatiquement à la largeur du QLabel
        self.drink_name.setTextInteractionFlags(Qt.TextSelectableByMouse)  # Rend le texte sélectionnable par la souris

        layout = QHBoxLayout(self)  # Ajouter un QHBoxLayout au widget
        layout.addWidget(self.drink_name)

    def update(self):
        db,index = RU.boisson_choisie
        boisson = Db.dbsall[db][0].iloc[index]
        db_utilisee = Db.choisir_db(db,0)
        index_name = db_utilisee.columns.get_loc('Name')
        if str(boisson[index_name]) != 'nan' and str(boisson[index_name]) != '':
            drink_name = boisson[index_name]
        else :
            drink_name = 'Nom non renseigné'
        self.drink_name.setText(f'<font color="red"><b>Boisson : {drink_name}</b></font>')


class InformationsDisplay(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.description_text = QLabel()
        self.description_text.setWordWrap(True)  # Pour que le texte s'ajuste automatiquement à la largeur du QLabel
        self.description_text.setTextInteractionFlags(Qt.TextSelectableByMouse)  # Rend le texte sélectionnable par la souris

        image_label = QLabel()
        image_label.setFixedSize(300,40)
        # image_label.setPixmap(QPixmap("codes/UI/Icones/boisson.jpg"))

        self.addWidget(self.description_text)
        self.addWidget(image_label)

    def update(self):
        db,index = RU.boisson_choisie
        db_utilisee = Db.dbsall[db][0]
        boisson = db_utilisee.iloc[index]

        formatted_text = self.format_text(boisson, db_utilisee)
        self.description_text.setText(formatted_text)

    # Mettre dans le backend cette fonction
    def format_text(self, boisson, db_utilisee):
        formatted_lines = []
        column_index = []
        
        # Wines
        if RU.choix_de_la_data_base == 0:
            real_names = ['country', 'description', 'price', 'province', 'variety', 'winery', 'region_']
            column_names = ['Provenance', 'Description', 'Prix', 'Province', 'Variété', 'Domaine', 'Région']
        # Cocktails
        elif RU.choix_de_la_data_base == 1: 
            real_names = ['strAlcoholic', 'strCategory', 'strDrinkThumb', 'strGlass', 'strIBA', 'strIngredient', 'strMeasure', 'strInstructions', 'strVideo']
            column_names = ['Type (Alcoholic/Non Alcoholic)', 'Catégorie', 'Lien Image Verre', 'Type de verre', 'strIBA', 'Ingrédients', 'Quantités', 'Préparation', 'Vidéo']
        # Beers
        elif RU.choix_de_la_data_base == 2: 
            real_names = ['brewery_name', 'beer_style', 'review_aroma', 'review_appearance', 'review_palate', 'review_taste', 'review_time','review_overall']
            column_names = ['Brasseur', 'Style', 'Arômes', 'Apparence', 'Palais', 'Goût', 'Nombre d''évaluations', 'Review globale']
        # Coffee
        elif RU.choix_de_la_data_base == 3: 
            real_names = ['loc_country', 'roaster', 'roast', '100g_USD', 'origin_', 'desc_', 'rating']
            column_names = ['Provenance', 'Torréfacteur', 'Torréfaction', 'Prix', 'Origine', 'Description', 'Note (/100)']
        # Mocktails
        elif RU.choix_de_la_data_base == 4:
            real_names = ['Ingredient ', 'Flavor Profile ', 'User Rating']
            column_names = ['Ingrédients', 'Saveurs', 'Note (/5)']

        #Création de la liste d'index pour récupérer les données
        for name in real_names:
                index = db_utilisee.columns.get_loc(name)
                column_index.append(index)

        #Récupération des données et mise en forme
        for i in range(len(column_index)):
            index = column_index[i]
            column_name = column_names[i]
            value = boisson[index]

            # Convertir la valeur en chaîne de caractères
            if isinstance(value, list):
                value_str = ', '.join(str(item) for item in value)
            elif column_name == 'Prix' and str(value) != 'nan':
                if RU.choix_de_la_data_base == 0 : 
                    value_str = f"{value} €"
                elif RU.choix_de_la_data_base == 3: 
                    value_str = f"{value} USD/100g"
            else:
                value_str = str(value)

            if value_str.startswith('[') and value_str.endswith(']'):
                value_list = [item.strip("' ") for item in value_str[1:-1].split(',')]
                seen_elements = set()
                value_list_filtered = [item for item in value_list if item != 'nan' and item != '' and item != ' ' and (item not in seen_elements and seen_elements.add(item) is None)]
                value_str = ', '.join(value_list_filtered)
            
            if RU.choix_de_la_data_base == 2 and column_name == 'Arômes':
                formatted_lines.append(f"Evaluations (/5) : ")
                remaining_elements = [col for col in column_names[i+1:]]
                for element in remaining_elements:
                    if element == 'Nombre d''évaluations':
                        formatted_lines.append(f"\n   - {element} : {int(boisson[column_index[column_names.index(element)]]):,}")
                    else :
                        formatted_lines.append(f"\n   - {element} : {boisson[column_index[column_names.index(element)]]:,}")
            elif column_name not in ['Apparence', 'Palais', 'Goût', 'Nombre d''évaluations', 'Review globale'] and value_str != 'nan':
                formatted_line = f"{column_name} : {value_str}"
                formatted_lines.append(formatted_line)
                formatted_lines.append('')

        return '\n'.join(formatted_lines)

##BENE  
class FavoriteInteraction(QPushButton):
    def __init__(self):
        super().__init__()

        self.star_icon_empty = QIcon("codes/UI/Icones/star_empty.png")
        self.star_icon_filled = QIcon("codes/UI/Icones/star_filled.png")

        self.setText('Ajouter en Favori')
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.clicked.connect(self.update_status)
        self.setIcon(self.star_icon_empty)
        
    def update_icon(self):
        
        db,index = RU.boisson_choisie
        favory = Db.dbsall[db][0].iloc[index][-1]

        if favory:
            self.setIcon(self.star_icon_filled)
        else:
            self.setIcon(self.star_icon_empty)

    def update_status(self):
        db,index = RU.boisson_choisie
        favory = not(Db.dbsall[db][0].iloc[index][-1])
        Db.dbsall[db][0].iloc[index,-1] = favory
        self.update_icon()


##BENE
class CommentInteracton(QHBoxLayout):
    def __init__(self):
        super().__init__()

        bouton = QPushButton('Commenter')
        bouton.setIcon(QIcon("codes/UI/Icones/comment.png"))
        bouton.setStyleSheet("background-color: #404040; color: #ffffff;")
        bouton.clicked.connect(self.update)

        self.texte = QLineEdit()
        self.update()
        
        self.addWidget(bouton)
        self.addWidget(self.texte)


    def update(self):
        commentaire = "OUIIIIII"

        if   pd.isna(commentaire):
            self.texte.setPlaceholderText('Laisser un commentaire sur votre boisson')
        else :
            self.texte.setPlaceholderText(commentaire)


class RatingInteraction(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText(' Noter')
        self.setIcon(QIcon("codes/UI/Icones/rate.png"))
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.clicked.connect(self.open_rating_page)

    def open_rating_page(self):
        rating_page = DrinkRatingPage("OK", QSize(500,1000))
        rating_page.show()
    
    def update(self):
        pass


class DrinkRatingPage(QWidget):
    def __init__(self, drink_name, parent_size):
        super().__init__()
        self.drink_name = drink_name
        self.setWindowTitle("Noter la boisson")

        self.setWindowOpacity(0.95) # Rendre la fenêtre transparente
        self.setGeometry(200, 200, parent_size.height(), parent_size.width())
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


##BENE
class NotationsInteractions(QVBoxLayout):
    def __init__(self, ):
        super().__init__()

        self.favorite_interaction = FavoriteInteraction()
        self.rating_interaction = RatingInteraction()
        self.comment_interaction = CommentInteracton()
        int_layout = QHBoxLayout()


        int_layout.addWidget(self.favorite_interaction)
        int_layout.addWidget(self.rating_interaction)

        self.addLayout(int_layout)
        self.addLayout(self.comment_interaction)

    def update(self):
        self.favorite_interaction.update_icon()
        self.rating_interaction.update()
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
        info_layout.addLayout(self.informations_display)
        info_layout.addStretch()
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
    
