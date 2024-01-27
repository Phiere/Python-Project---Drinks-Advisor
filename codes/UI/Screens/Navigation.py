import sys
from PyQt5.QtGui import  QIcon
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, 
                            QStackedWidget,QHBoxLayout)


import Loading_page as LP
import Research_page_UI as RU
import Profil_page_UI as PU
import Creation_page_UI as CU
import Description_page as DU


class MenuButton(QPushButton):
    def __init__(self,stack_control,stack_index,path_icone) :
        super().__init__()
        self.setIcon(QIcon(path_icone))
        self.setFixedSize(40,40)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.pressed.connect(lambda : stack_control(stack_index))
    

class MenuLayout(QHBoxLayout): 
    def __init__(self,stack_control) :
        super().__init__()        
  
        buton_back = MenuButton(stack_control,0,"codes/UI/Icones/back.png")
        buton_creation = MenuButton(stack_control,2,"codes/UI/Icones/plus.png")
        buton_profile = MenuButton(stack_control,1,"codes/UI/Icones/profile.png")

        self.addWidget(buton_back)
        self.addWidget(buton_creation)
        self.addStretch()
        self.addWidget(buton_profile)


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


class DisplayerScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DrinksAdvisor App")
        self.setStyleSheet("background-color: #1f1f1f;")
        
        window_layout = QVBoxLayout()
        menu_bar = MenuLayout(self.goToScreen)
        self.screens_to_display = ScreensToDisplay(show_description = lambda : self.goToScreen(3))

        window_layout.addLayout(menu_bar)
        window_layout.addWidget(self.screens_to_display)
        self.setLayout(window_layout)


    def goToScreen(self, index):
        if index == 3 :
            self.screens_to_display.description_screen.update()
        self.screens_to_display.setCurrentIndex(index)

############

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
    main_window = DisplayerScreen()
    main_window.show()

if __name__ == '__main__':
    main()
