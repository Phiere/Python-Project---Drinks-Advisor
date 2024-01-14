import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget,QHBoxLayout

import Research_page_UI as RU
import Description_page as DP




class ComposeDisplay(QStackedWidget):
    def __init__(self):
        super().__init__()


        research_screen = RU.ScreenResearch(lambda : self.goToScreen(1))
        self.description_screen = DP.Description(lambda : self.goToScreen(0))
        
        self.addWidget(research_screen)
        self.addWidget(self.description_screen)
    
    def goToScreen(self,index):

        self.description_screen.update()
        self.setCurrentIndex(index)



class Composee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exploration')
        self.resize(1000,500)

        final_layout = QVBoxLayout()

        self.screens_to_display = ComposeDisplay()


        final_layout.addWidget(self.screens_to_display)
        self.setLayout(final_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main_window = Composee()
    main_window.show()
    
    sys.exit(app.exec_())
