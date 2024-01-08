import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

class ClickableContainer(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QHBoxLayout and set it as the layout for this widget
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)

        # Add some widgets to the layout
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        self.layout.addWidget(button1)
        self.layout.addWidget(button2)

    def mousePressEvent(self, event):
        print("Mouse clicked on the container!")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    container = ClickableContainer()
    container.show()

    sys.exit(app.exec_())
