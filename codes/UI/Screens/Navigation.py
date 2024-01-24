import sys
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget,QHBoxLayout

import Loading_page as LP
import Research_page_UI as RU
import Profil_page_UI as PU
import Creation_page_UI as CU
import Description_page as DU


class MenuLayout(QHBoxLayout): 
    def __init__(self,fenetre_totale) -> None:
        super().__init__()

        boutonRetour = QPushButton()
        boutonRetour.setIcon(QIcon("codes/UI/Icones/back.png"))
        boutonRetour.setFixedSize(40, 40)
        boutonRetour.setStyleSheet("background-color: #404040; color: #ffffff;")

        boutonCreation = QPushButton()
        boutonCreation.setIcon(QIcon("codes/UI/Icones/plus.png"))
        boutonCreation.setFixedSize(40, 40)
        boutonCreation.setStyleSheet("background-color: #404040; color: #ffffff;")

        boutonSettings = QPushButton()
        boutonSettings.setIcon(QIcon("codes/UI/Icones/profile.png"))
        boutonSettings.setFixedSize(40, 40)
        boutonSettings.setStyleSheet("background-color: #404040; color: #ffffff;")

        self.addWidget(boutonRetour)
        self.addWidget(boutonCreation)
        self.addStretch()
        self.addWidget(boutonSettings)

        boutonRetour.pressed.connect(lambda : fenetre_totale.goToScreen(0))
        boutonSettings.pressed.connect(lambda : fenetre_totale.goToScreen(1))
        boutonCreation.pressed.connect(lambda : fenetre_totale.goToScreen(2))

class ScreensToDisplay(QStackedWidget):
    def __init__(self,show_description):
        super().__init__()

        research_screen = RU.ScreenResearch(show_description)
        profil_screen = PU.ScreenProfile()
        creation_screen = CU.ScreenCreation()
        self.description_screen = DU.Description()

        self.addWidget(research_screen)
        self.addWidget(profil_screen)
        self.addWidget(creation_screen)
        self.addWidget(self.description_screen)

class FenetrePrincipale(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DrinksAdvisor App")
        self.setStyleSheet("background-color: #1f1f1f;")
        
        final_layout = QVBoxLayout()

        Barre_menu = MenuLayout(self)
        self.screens_to_display = ScreensToDisplay(show_description = lambda : self.goToScreen(3))

        final_layout.addLayout(Barre_menu)
        final_layout.addWidget(self.screens_to_display)
        self.setLayout(final_layout)


    def goToScreen(self, index):
        if index == 3 :
            self.screens_to_display.description_screen.update()
        self.screens_to_display.setCurrentIndex(index)

def main():
    app = QApplication(sys.argv)

    # Étape 1: Afficher l'écran de chargement
    loading_screen = LP.LoadingScreen()
    # Connecter la fonction show_main_window à l'événement de chargement terminé
    loading_screen.loading_completed.connect(show_main_window)
    loading_screen.show()
    sys.exit(app.exec_())

def show_main_window():
    # Étape 2: Charger l'application principale une fois le chargement terminé
    main_window = FenetrePrincipale()
    main_window.show()

if __name__ == '__main__':
    main()
