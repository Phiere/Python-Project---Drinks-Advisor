import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget,QHBoxLayout
import Reasearch_page_creation_UI as RU
import Home_page_creation as HC
import Profil_page_UI as PU


class MenuLayout(QWidget): 
    def __init__(self) -> None:
        super().__init__()

        

        self.menuLayout = QHBoxLayout()
        boutonAcceuil = QPushButton('Home')
        boutonRetour = QPushButton('Back')
        boutonSettings = QPushButton('Settings')
        self.menuLayout.addWidget(boutonAcceuil)
        self.menuLayout.addWidget(boutonRetour)
        self.menuLayout.addWidget(boutonSettings)
"""
        boutonAcceuil.pressed.connect(self.go_to_acceuil)
        boutonRetour.pressed.connect(self.go_to_research)
        boutonSettings.pressed.connect(self.go_to_profile)
    
    def go_to_acceuil(self):
        self.navigateur.current_screen_index = 0
    def go_to_research(self):
        self.navigateur.current_screen_index = 1
    def go_to_profile(self):
        self.navigateur.current_screen_index = 2"""




class FenetrePrincipale(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)
        self.Home_screen = HC.ScreenHomeWindow()
        self.research_screen = RU.ScreenResearch()
        self.profil_screen = PU.ScreenProfile()

        self.stacked_widget.addWidget(self.Home_screen)
        self.stacked_widget.addWidget(self.research_screen)
        self.stacked_widget.addWidget(self.profil_screen)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        self.current_screen_index = 0

    def next_screen(self):
        self.stacked_widget.setCurrentIndex(self.current_screen_index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main_window = FenetrePrincipale()
    main_window.show()
    
    sys.exit(app.exec_())
