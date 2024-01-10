import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget,QHBoxLayout

import Research_page_UI as RU
import Profil_page_UI as PU
import Creation_page_UI as CU
import Description_page as DU

class MenuLayout(QHBoxLayout): 
    def __init__(self,fenetre_totale) -> None:
        super().__init__()


        boutonRetour = QPushButton('Explore')
        boutonCreation = QPushButton('Creation')
        boutonSettings = QPushButton('Profile')
    
        self.addWidget(boutonRetour)
        self.addWidget(boutonCreation)
        self.addWidget(boutonSettings)

        boutonRetour.pressed.connect(lambda : fenetre_totale.goToScreen(0))
        boutonSettings.pressed.connect(lambda : fenetre_totale.goToScreen(1))
        boutonCreation.pressed.connect(lambda : fenetre_totale.goToScreen(2))

class ScreensToDisplay(QStackedWidget):
    def __init__(self):
        super().__init__()

        research_screen = RU.ScreenResearch()
        profil_screen = PU.ScreenProfile()
        creation_screen = CU.ScreenCreation()
        description_screen = DU.Description('Nom Page')

        self.addWidget(research_screen)
        self.addWidget(profil_screen)
        self.addWidget(creation_screen)
        self.addWidget(description_screen)

class FenetrePrincipale(QWidget):
    def __init__(self):
        super().__init__()

        final_layout = QVBoxLayout()

        Barre_menu = MenuLayout(self)
        self.screens_to_display = ScreensToDisplay()

        final_layout.addLayout(Barre_menu)
        final_layout.addWidget(self.screens_to_display)
        self.setLayout(final_layout)


    def goToScreen(self, index):
        self.screens_to_display.setCurrentIndex(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main_window = FenetrePrincipale()
    main_window.show()
    
    sys.exit(app.exec_())
