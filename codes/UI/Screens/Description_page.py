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
        db =  Db.choix_de_la_data_base
        index = Db.index_boisson
        boisson = Db.dbsall[db][0].iloc[index]
        db_utilisee = Db.dbsall[db][0]
        index_name = db_utilisee.columns.get_loc('Name')
        if str(boisson[index_name]) != 'nan' and str(boisson[index_name]) != '':
            drink_name = boisson[index_name]
        else :
            drink_name = 'Nom non renseigné'
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

        self.setFixedSize(1000, 350)

    def update(self):
        db =    Db.choix_de_la_data_base
        index = Db.index_boisson
        db_utilisee = Db.dbsall[db][0]
        boisson = db_utilisee.iloc[index]

        formatted_text = self.format_text(boisson, db_utilisee)
        self.description_text.setText(formatted_text)

    # Mettre dans le backend cette fonction
    def format_text(self, boisson, db_utilisee):
        formatted_lines = []
        column_index = []
        
        # Wines
        if Db.choix_de_la_data_base == 0:
            real_names = ['country', 'description', 'price', 'province', 'variety', 'winery', 'region_']
            column_names = ['Provenance', 'Description', 'Prix', 'Province', 'Variété', 'Domaine', 'Région']
        # Cocktails
        elif Db.choix_de_la_data_base == 1: 
            real_names = ['strAlcoholic', 'strCategory', 'strDrinkThumb', 'strGlass', 'strIBA', 'strIngredient', 'strMeasure', 'strInstructions', 'strVideo']
            column_names = ['Type (Alcoholic/Non Alcoholic)', 'Catégorie', 'Lien Image Verre', 'Type de verre', 'strIBA', 'Ingrédients', 'Quantités', 'Préparation', 'Vidéo']
        # Beers
        elif Db.choix_de_la_data_base == 2: 
            real_names = ['brewery_name', 'beer_style', 'review_aroma', 'review_appearance', 'review_palate', 'review_taste', 'review_time','review_overall']
            column_names = ['Brasseur', 'Style', 'Arômes', 'Apparence', 'Palais', 'Goût', 'Nombre d''évaluations', 'Review globale']
        # Coffee
        elif Db.choix_de_la_data_base == 3: 
            real_names = ['loc_country', 'roaster', 'roast', '100g_USD', 'origin_', 'desc_', 'rating']
            column_names = ['Provenance', 'Torréfacteur', 'Torréfaction', 'Prix', 'Origine', 'Description', 'Note (/100)']
        # Mocktails
        elif Db.choix_de_la_data_base == 4:
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
                if Db.choix_de_la_data_base == 0 : 
                    value_str = f"{value} €"
                elif Db.choix_de_la_data_base == 3: 
                    value_str = f"{value} USD/100g"
            else:
                value_str = str(value)

            if value_str.startswith('[') and value_str.endswith(']'):
                value_list = [item.strip("' ") for item in value_str[1:-1].split(',')]
                seen_elements = set()
                value_list_filtered = [item for item in value_list if item != 'nan' and item != '' and item != ' ' and (item not in seen_elements and seen_elements.add(item) is None)]
                value_str = ', '.join(value_list_filtered)
            
            if Db.choix_de_la_data_base == 2 and column_name == 'Arômes':
                formatted_lines.append(f"Evaluations (/5) : ")
                remaining_elements = [col for col in column_names[i+1:]]
                for element in remaining_elements:
                    if element == 'Nombre d''évaluations':
                        formatted_lines.append(f"\n   - {element} : {int(boisson[column_index[column_names.index(element)]]):,}")
                    else :
                        formatted_lines.append(f"\n   - {element} : {boisson[column_index[column_names.index(element)]]:,}")
            elif column_name not in ['Apparence', 'Palais', 'Goût', 'Nombre d''évaluations', 'Review globale'] and value_str != 'nan'and value_str != '' and value_str != ' ':
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
        self.setFixedSize(1000,40)

    def update_icon(self):
        
        db =  Db.choix_de_la_data_base
        index = Db.index_boisson
        favory = Db.dbsall[db][0].iloc[index][-1]

        if favory:
            self.setIcon(self.star_icon_filled)
        else:
            self.setIcon(self.star_icon_empty)

    def update_status(self):
        db =  Db.choix_de_la_data_base
        index = Db.index_boisson
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
        bouton.clicked.connect(self.comment)
        bouton.setFixedSize(150,40)

        self.texte = QLineEdit()
        self.texte.setFixedSize(850,40)
        
        self.addWidget(bouton)
        self.addWidget(self.texte)


    def update(self):
        db =  Db.choix_de_la_data_base
        index = Db.index_boisson
        commentaire = Db.dbsall[db][0].iloc[index][-2]
        self.texte.setText('')
        if   pd.isna(commentaire):
            self.texte.setPlaceholderText('Laisser un commentaire sur votre boisson')
        else :
            self.texte.setPlaceholderText(commentaire)
    
    def comment(self):
        db =  Db.choix_de_la_data_base
        index = Db.index_boisson
        Db.dbsall[db][0].iloc[index,-2] = self.texte.text()


class RatingInteraction(QWidget):
    def __init__(self):
        super().__init__()
        rate_button = QPushButton(' Noter')
        rate_button.setIcon(QIcon("codes/UI/Icones/rate.png"))
        rate_button.setFixedSize(80,40)
        rate_button.setStyleSheet("background-color: #404040; color: #ffffff;")
        rate_button.clicked.connect(self.update_status)

        stars_layout = QHBoxLayout()

        self.stars_images = []
        for i in range(1, 6):
            empty_star = QPixmap("codes/UI/Icones/star_empty.png").scaled(40, 40)
            filled_star = QPixmap("codes/UI/Icones/star_filled.png").scaled(40, 40)
            self.stars_images.append((empty_star, filled_star))

        self.rating = 0

        self.star_buttons = []
        for i in range(5):
            star_button = QPushButton()
            star_button.setIcon(QIcon(self.stars_images[i][0]))
            star_button.setFixedSize(80, 40)
            star_button.clicked.connect(lambda _, idx=i + 1: self.on_star_click(idx))
            star_button.installEventFilter(self)
            self.star_buttons.append(star_button)

            # Ajoute chaque étoile au layout horizontal
            stars_layout.addWidget(star_button)

        # Ajoute le bouton "Noter" et le layout des étoiles à ce widget
        main_layout = QHBoxLayout()
        main_layout.addStretch()
        main_layout.addWidget(rate_button)
        main_layout.addLayout(stars_layout)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def on_star_click(self, index):
        if index > self.rating:
            for i in range(index):
                self.star_buttons[i].setIcon(QIcon(self.stars_images[i][1]))
        else:
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
    
    def update_icon(self):
        db =  Db.choix_de_la_data_base
        index = Db.index_boisson
        rating = Db.dbsall[db][0].iloc[index][-3]
        self.on_star_click(int(rating))

    def update_status(self):
        db =  Db.choix_de_la_data_base
        index = Db.index_boisson
        Db.dbsall[db][0].iloc[index,-3] = self.rating
        self.update_icon()

##BENE
class NotationsInteractions(QVBoxLayout):
    def __init__(self, ):
        super().__init__()

        self.favorite_interaction = FavoriteInteraction()
        self.rating_interaction = RatingInteraction()
        self.comment_interaction = CommentInteracton()


        self.addWidget(self.favorite_interaction)
        self.addWidget(self.rating_interaction)
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
    
