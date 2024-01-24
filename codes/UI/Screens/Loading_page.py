from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
from PyQt5.QtCore import QTimer, QPointF, Qt, QObject, pyqtSignal
from PyQt5.QtGui import QColor, QTransform
import sys
import Navigation  # Importez le module Navigation.py

class LoadingScreen(QGraphicsView):
    loading_completed = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chargement de l'application")
        self.setGeometry(200, 200, 1050, 720)
        self.setStyleSheet("background-color: #333333; color: white;")

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Paramètres de l'animation
        self.radius = 20
        self.num_points = 5  # Modifiez le nombre de points selon vos besoins
        self.rotation_time = 0.5  # Temps en secondes pour un tour complet des points
        self.total_duration = 6  # Temps total en secondes pour le chargement complet
        self.timer_interval = 50  # Ajustez cet intervalle pour maintenir la vitesse de rotation des points

        # Calcul de l'angle par étape pour obtenir une vitesse de 1 tour/s pour les points
        self.angle_step = 270 / self.total_duration 

        # Création des éléments graphiques
        self.create_loading_points()

        # Timer pour mettre à jour l'animation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(self.timer_interval)

        # Compteur pour suivre le nombre de frames écoulées
        self.frame_count = 0

        # Démarrer la fenêtre de chargement
        self.show()

    def create_loading_points(self):
        self.loading_points = []
        for i in range(self.num_points):
            point = QGraphicsEllipseItem(-2.5, -2.5, 5, 5)  # Ajustez la taille des points selon vos besoins
            point.setBrush(QColor(255, 255, 255))

            # Calculez la position initiale de chaque point sur le cercle
            initial_angle = i * (360 / self.num_points)
            initial_position = QTransform().rotate(initial_angle).map(QPointF(self.radius, 0))

            point.setPos(initial_position)
            self.loading_points.append(point)
            self.scene.addItem(point)

    def update_animation(self):
        # Calculer le pourcentage de chargement en fonction du nombre de frames écoulées
        percentage = (self.frame_count * self.timer_interval / (self.total_duration * 1000)) * 100

        # Mettre à jour la position des points en fonction du pourcentage
        rotation = self.angle_step * (self.frame_count % int(self.total_duration * 1000 / self.timer_interval))
        for i, point in enumerate(self.loading_points):
            angle = rotation + i * (self.angle_step / (self.num_points - 1))
            transform = QTransform().rotate(angle)
            rotated_point = transform.map(QPointF(self.radius, 0))
            point.setPos(rotated_point)

        # Incrémenter le compteur de frames
        self.frame_count += 1

        # Si le chargement atteint 100%, lancer le code Navigation.py
        if percentage >= 100 and self.frame_count >= int(self.total_duration * 1000 / self.timer_interval):
            self.timer.stop()  # Arrêter le timer
            self.close()  # Fermer la fenêtre de chargement
            self.loading_completed.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    loading_screen = LoadingScreen()

    sys.exit(app.exec_())
