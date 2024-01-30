import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsPixmapItem, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

class CircleAnimation(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Animation de cercle')

        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(Qt.black)

        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(10, 10, 380, 380)

        self.circle_item = QGraphicsEllipseItem(0, 0, 0, 0)
        pen = self.circle_item.pen()
        pen.setColor(Qt.white)
        self.circle_item.setPen(pen)
        
        self.scene.addItem(self.circle_item)

        self.pixmap_item = QGraphicsPixmapItem()
        self.scene.addItem(self.pixmap_item)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateAnimation)

        self.show()

        # Atteindre un diamètre de 35 en 1 seconde (1000 ms)
        self.animation_duration = 1000
        self.animation_step = 0
        self.animation_steps = int(self.animation_duration / 100)

        self.timer.start(100)  # Démarrer la mise à jour toutes les 100 ms

    def updateAnimation(self):
        progress = self.animation_step / self.animation_steps

        # Calculer la nouvelle taille du cercle pour atteindre un diamètre de 35
        new_size = 35 * progress
        self.circle_item.setRect(0, 0, new_size, new_size)

        if progress >= 1.0:
            # Charger l'icône et la redimensionner à 50x50 pixels
            pixmap = QPixmap("codes/UI/Icones/valide.png").scaled(36, 36, Qt.KeepAspectRatio)
            self.pixmap_item.setPixmap(pixmap)

        if self.animation_step < self.animation_steps:
            self.animation_step += 1
        else:
            self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleAnimation()
    sys.exit(app.exec_())
