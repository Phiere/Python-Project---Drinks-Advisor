from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer

class MyApp(QPushButton):
    def __init__(self):
        super().__init__()

        self.setText("Appuyez longuement sur moi")
        self.button.pressed.connect(self.on_pressed)
        self.button.released.connect(self.on_released)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # 2000 ms = 2 secondes
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.on_long_press)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

    def on_pressed(self):
        self.timer.start()

    def on_released(self):
        if self.timer.isActive():
            self.timer.stop()

    def on_long_press(self):
        print("Le bouton a été pressé longuement.")

app = QApplication([])
window = MyApp()
window.show()
app.exec_()
