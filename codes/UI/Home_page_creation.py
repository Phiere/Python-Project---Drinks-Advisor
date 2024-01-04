from Importations import *

    
class ScreenHomeWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Home Window")
        self.resize(1000,600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        globalLayout = QVBoxLayout()
        alccolLayout = QHBoxLayout()
        alcoolfreeLayout = QHBoxLayout()

        
        alcoolTitle = QLabel("alcool")
        alcoolTitle.setFrameStyle(QFrame.Box | QFrame.Plain)
        font = alcoolTitle.font()
        font.setBold(True)
        alcoolTitle.setFont(font)
        alcoolfreeTitle = QLabel("sans alcool")
        alcoolfreeTitle.setFrameStyle(QFrame.Box | QFrame.Plain)
        font = alcoolfreeTitle.font()
        font.setBold(True)
        alcoolfreeTitle.setFont(font)

        winebutton = QPushButton("Vin")
        winebutton.setSizePolicy(sizePolicy)
        beerbutton = QPushButton("Bière")
        beerbutton.setSizePolicy(sizePolicy)
        cocktailbutton = QPushButton("Cocktail")
        cocktailbutton.setSizePolicy(sizePolicy)

        coffebutton = QPushButton("Café")
        coffebutton.setSizePolicy(sizePolicy)
        theabutton = QPushButton("Thé")
        theabutton.setSizePolicy(sizePolicy)
        mocktailbutton = QPushButton("Mocktail")
        mocktailbutton.setSizePolicy(sizePolicy)

        alccolLayout.addWidget(winebutton)
        alccolLayout.addWidget(beerbutton)
        alccolLayout.addWidget(cocktailbutton)

        alcoolfreeLayout.addWidget(coffebutton)
        alcoolfreeLayout.addWidget(theabutton)
        alcoolfreeLayout.addWidget(mocktailbutton)

        globalLayout.addWidget(alcoolTitle)
        globalLayout.addLayout(alccolLayout)
        globalLayout.addWidget(alcoolfreeTitle)
        globalLayout.addLayout(alcoolfreeLayout)

        self.setLayout(globalLayout)


   

def main():
    app = QApplication(sys.argv)
    fenetre = ScreenHomeWindow()
    fenetre.show()
    app.exec()

if __name__ == '__main__':
    main()