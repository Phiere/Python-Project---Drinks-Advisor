############################################################
############################################################
############################################################
# Création de la page de description rassemblant les éléments de description de la boisson choisie ainsi que les 
# élements de notations
############################################################
############################################################
############################################################

import sys
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QLabel,QHBoxLayout,QWidget,QApplication,QVBoxLayout,QScrollArea,QPushButton,QLineEdit
from PyQt5.QtCore import Qt

sys.path.append('codes/BackEnd/')
import Description_page_back as Dp


class LabelPrincipal(QWidget):
    """Label mettant en valeur le nom principal de la boisson
    
    - update : met à jour le nom en fonction de la boisson choisie"""
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: #1f1f1f;")

        self.drink_name = QLabel()
        self.drink_name.setWordWrap(True)  # Pour que le texte s'ajuste automatiquement à la largeur du QLabel
        self.drink_name.setTextInteractionFlags(Qt.TextSelectableByMouse)  # Rend le texte sélectionnable par la souris
        self.drink_name.setFixedHeight(40)
        layout = QHBoxLayout(self)  # Ajouter un QHBoxLayout au widget
        layout.addWidget(self.drink_name)
        self.update()

    def update(self):
        drink_name = Dp.get_name_from_drink()
        self.drink_name.setText(f'<font color="red"><b>Drink : {drink_name}</b></font>')


class InformationsDisplay(QScrollArea):
    """Affichage des informations de la boisson choisie
    
    - update : met à jours les informations affichées en fonction de la boisson choisie"""
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
        self.update()

    def update(self):
        texte =  Dp.get_description_from_drink()
        self.description_text.setText(texte)


class FavoriteInteraction(QPushButton):
    """Bouton de sélection des favories. 
    
    - update-icon : met à jour l'icône du bouton en fonction du statut de favori
    - update_status : chanhe le statut de l'état favorie vers sont opposé"""
    def __init__(self):
        super().__init__()

        self.star_icon_empty = QIcon("codes/UI/Icones/star_empty.png")
        self.star_icon_filled = QIcon("codes/UI/Icones/star_filled.png")

        self.setText('Add to Favorites')
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
    """Affiche une interface pour commenter la boisson choisie
    
    - update : met à jour le texte du commentaire avec le commentaire de la boison choisie
    - comment : met à jour le commentaire avec le texte rentré"""
    def __init__(self):
        super().__init__()

        bouton = QPushButton('Comment')
        bouton.setIcon(QIcon("codes/UI/Icones/comment.png"))
        bouton.setStyleSheet("background-color: #404040; color: #ffffff;")
        bouton.clicked.connect(self.comment)
        bouton.setFixedSize(150,40)

        self.texte = QLineEdit()
        self.texte.setFixedHeight(40)
        self.setStretchFactor(self.texte, 6)
        
        self.addWidget(bouton)
        self.addWidget(self.texte)
        self.update()


    def update(self):
        self.texte.setText('')
        commentaire =  Dp.get_comment()
        if commentaire == "Unfilled" :
            self.texte.setPlaceholderText("Don't hesitate to comment !")
        else : self.texte.setText(commentaire)
    
    def comment(self):
        Dp.update_comment(self.texte.text())


class RatingInteraction(QHBoxLayout):
    """Affiche une interface pour noter la boisson choisie
    
    - on_star_click : enregistre la note attribuée à la boisson lors du clic sur une des étoiles
    - eventFilter : met à jour la couleur des étoiles lors du passage du curseur dessus
    - update_icon : met à jour l'icone (=la couleur) des étoiles de notation en fonction de la notation attribuée
    - update_status : met à jour la note attribuée à la boisson dans la database correspondante"""
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

        self.addStretch(5)
        for i in range(5):
            star_button = QPushButton()
            star_button.setIcon(QIcon(self.stars_images[i][0]))
            #star_button.setFixedSize(80, 40)
            star_button.setFixedHeight(40)
            star_button.clicked.connect(lambda _, idx=i + 1: self.update_status(idx))
            star_button.installEventFilter(self)
            self.star_buttons.append(star_button)

            # Ajoute chaque étoile au layout horizontal
            self.addWidget(star_button)
            self.setStretchFactor(star_button,1)
        self.addStretch(5)

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
    """Assemblage vertical des différents éléments de notation"""
    def __init__(self):
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


class GoEditButton(QPushButton):
    """Bouton déclancheur de l'édition de la boisson choisie
    
    - go_to_edit : fonction d'appel de l'écran d'édition"""
    def __init__(self,go_to_edit):
        super().__init__()
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.setText("Edit")
        self.clicked.connect(go_to_edit)


class Description(QWidget):
    """Ecran d'assemblage des différents élément de description : appel à l'édition, nom princpal, éléments de description, éléments de notation
    
    - show_edit : fonction d'appel à l'écran d'édition"""
    def __init__(self,show_edit):
        super().__init__()
        self.setStyleSheet("background-color: #1f1f1f; color: #ffffff;")
        self.setWindowTitle('Drink Description')
        self.setGeometry(200,200,1000,500)


        self.drink_name = LabelPrincipal()
        self.edit_button = GoEditButton(show_edit)
        self.informations_display = InformationsDisplay()
        self.notations_interactions = NotationsInteractions()
        info_layout = QVBoxLayout()
  
        info_layout.addWidget(self.drink_name)
        info_layout.addWidget(self.edit_button)
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
# Test : Les test pour l'interface utilisateur se feront en constatant
        #visuellement si les actions sont effectuées. Les test suivants doivent 
        #être réalisés.
# - 1 : La feneêtre respecte l'affichage du cahier des charges
# - 2 : La fenêtre affiche les éléments de la boisson choisie ainsi que le nom des colonnes correspondante      
# - 3 : Les éléments de description sont scrollable
# - 4 : les boutons de notation et de mise en favori change d'état lorsqu'ils sont cliqués. 
# - 5 : La ligne de commentaire affiche le commentaire actuel ou "don't hesitate to comment !" si ce dernier est vide           
############################################################
############################################################
############################################################
                  

def display_test():
    
    app = QApplication(sys.argv)
    fenetre = Description(lambda : 1)
    fenetre.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test = input("Tester les fonctions du script ? (0/1) : ")
    if test : display_test()
    
