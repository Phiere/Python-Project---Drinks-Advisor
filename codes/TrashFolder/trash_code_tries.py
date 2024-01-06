import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget

class FirstScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QPushButton("Bouton sur le premier écran", clicked=self.next_screen))

    def next_screen(self):
        main_window.next_screen()

class SecondScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QPushButton("Bouton sur le deuxième écran", clicked=self.next_screen))

    def next_screen(self):
        main_window.next_screen()

class ThirdScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QPushButton("Bouton sur le troisième écran", clicked=self.next_screen))

    def next_screen(self):
        main_window.next_screen()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)
        self.first_screen = FirstScreen()
        self.second_screen = SecondScreen()
        self.third_screen = ThirdScreen()

        self.stacked_widget.addWidget(self.first_screen)
        self.stacked_widget.addWidget(self.second_screen)
        self.stacked_widget.addWidget(self.third_screen)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        self.current_screen_index = 0

    def next_screen(self):
        self.current_screen_index = (self.current_screen_index + 1) % self.stacked_widget.count()
        self.stacked_widget.setCurrentIndex(self.current_screen_index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec_())
