############################################################
############################################################
############################################################
#Script naviguation : instancie toutes les écrans créés dans les autres dossier du projet. 
#C'est ce script qui assemble tous les écrans pour les insérer dans la feêntre principale.
############################################################
############################################################
############################################################

import sys
from PyQt5.QtGui import  QIcon
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, 
                            QStackedWidget,QHBoxLayout)


import Loading_page as LP
import Research_page_UI as RU
import Profil_page_UI as PU
import Creation_page_UI as CU
import Description_page as DU
import Edit_page_UI as EU
sys.path.append('codes/BackEnd/')
import Db_gestions as Db



class MenuButton(QPushButton):
    """Bouton dirigeant vers la page mise en argument"""
    def __init__(self,stack_control,stack_index,path_icone) :
        super().__init__()
        self.setIcon(QIcon(path_icone))
        self.setFixedSize(40,40)
        self.setStyleSheet("background-color: #404040; color: #ffffff;")
        self.pressed.connect(lambda : stack_control(stack_index))


class MenuLayout(QHBoxLayout): 
    """Construit une ligne de  3 boutons pour naviguer entre les écrans du logiciel"""
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
    """Concaténion des différents écrans de l'application"""
    def __init__(self,go_to_screen):
        super().__init__()

        show_description = lambda : go_to_screen(3)
        show_edit = lambda : go_to_screen(4)

        research_screen = RU.ScreenResearch(show_description)
        self.profil_screen = PU.ScreenProfile(show_description)
        creation_screen = CU.ScreenCreation(show_description)
        self.description_screen = DU.Description(show_edit)
        self.edit_screen = EU.ScreenEdition(show_description)

        self.addWidget(research_screen)
        self.addWidget(self.profil_screen)
        self.addWidget(creation_screen)
        self.addWidget(self.description_screen)
        self.addWidget(self.edit_screen)


class DisplayerScreen(QWidget):
    """Fenêtre principale contenant le stack des écrans et les méthodes de naviguation
    
    - go_to_screen : permet de navuguer d'un écran à l'autre en restant sur la fenêtre principale"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DrinksAdvisor App")
        self.setStyleSheet("background-color: #1f1f1f;")
        
        window_layout = QVBoxLayout()
        menu_bar = MenuLayout(self.go_to_screen)
        self.screens_to_display = ScreensToDisplay(self.go_to_screen)

        window_layout.addLayout(menu_bar)
        window_layout.addWidget(self.screens_to_display)
        self.setLayout(window_layout)


    def go_to_screen(self, index):
        if index == 1 :
            self.screens_to_display.profil_screen.update()
        elif index == 3 :
            self.screens_to_display.description_screen.update()
        elif index == 4 : 
            self.screens_to_display.edit_screen.update()
        self.screens_to_display.setCurrentIndex(index)

    def closeEvent(self, event):
        #Db.changes_save()
        print("projet fini")
        

############################################################
############################################################
############################################################
# Test : Les tests pour l'interface utilisateur se feront en constatant
        #visuellement si les actions sont effectuées. Les tests suivants doivent 
        #être réalisés.
# - 1 : La navigation doit pourvoir se faire entre chaque page suivant les combinaisons suivante :
    # a : profil(toutes les pages) mène à l'écran profil
    # b : recherche(toutes les pages) mène à l'écran de recherche
    # c : création (toutes les pages) mène à l'écran de création
    # d : page recherche : page description est accessible en clqiuant sur une boisson
    # e : page édition : accessible en cliquant sur edit depuis description
# - 2 : quitter la fenetre principale enregistre les changement effectués
############################################################
############################################################
############################################################



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

