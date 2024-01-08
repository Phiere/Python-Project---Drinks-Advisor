import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget,QHBoxLayout
import Research_page_UI as RU
import Home_page_creation as HC
import Profil_page_UI as PU
import Creation_page_UI as CU
import Description_page as DU

class MenuLayout(QWidget): 
    def __init__(self,screens_call) -> None:
        super().__init__()


        self.menuLayout = QHBoxLayout()
        boutonAcceuil = QPushButton('Home')
        boutonRetour = QPushButton('Explore')
        boutonCreation = QPushButton('Creation')
        boutonSettings = QPushButton('Profile')
    
        self.menuLayout.addWidget(boutonRetour)
        self.menuLayout.addWidget(boutonCreation)
        self.menuLayout.addWidget(boutonSettings)

        boutonAcceuil.pressed.connect(screens_call[0])
        boutonRetour.pressed.connect(screens_call[1])
        boutonSettings.pressed.connect(screens_call[2])
        boutonCreation.pressed.connect(screens_call[3])
    

class FenetrePrincipale(QWidget):
    def __init__(self):
        super().__init__()

        screens_call = [self.HomeScreen,self.ReasearchScreen,self.ProfileScreen,self.CreationScreen]

        self.stacked_widget = QStackedWidget(self)
        self.Home_screen = HC.ScreenHomeWindow(screens_call)
        self.research_screen = RU.ScreenResearch(screens_call,self.DescriptionScreen)
        self.profil_screen = PU.ScreenProfile(screens_call)
        self.creation_screen = CU.ScreenCreation(screens_call)
        self.description_screen = DU.Description('Nom Page',screens_call)

        self.stacked_widget.addWidget(self.Home_screen)
        self.stacked_widget.addWidget(self.research_screen)
        self.stacked_widget.addWidget(self.profil_screen)
        self.stacked_widget.addWidget(self.creation_screen)
        self.stacked_widget.addWidget(self.description_screen)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        self.current_screen_index = 0

        
    def HomeScreen(self):
        self.stacked_widget.setCurrentIndex(0)
    def ReasearchScreen(self):
        self.stacked_widget.setCurrentIndex(1)
    def ProfileScreen(self):
        self.stacked_widget.setCurrentIndex(2)
    def CreationScreen(self):
        self.stacked_widget.setCurrentIndex(3)
    def DescriptionScreen(self):
        self.stacked_widget.setCurrentIndex(4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main_window = FenetrePrincipale()
    main_window.show()
    
    sys.exit(app.exec_())
