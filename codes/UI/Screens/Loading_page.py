from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
from PyQt5.QtCore import QTimer, QPointF, pyqtSignal
from PyQt5.QtGui import QColor, QTransform
import sys

class LoadingScreen(QGraphicsView):
    """ Création d'un écran de chargement avec des points qui tournent au milieu de l'écran
    
    - create_loading_points : crée plusieurs points qui vont se positionner au centre de l'écran en forme de cercle
    - update_animation : met à jour la position des points afin de créer l'animation de chargement (= les points tournent)"""
    loading_completed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loading...")
        self.resize(1000,500)
        self.setStyleSheet("background-color: #333333; color: white;")
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)


        self.radius = 20
        self.num_points = 5  
        self.rotation_time = 0.5  
        self.total_duration = 6  
        self.timer_interval = 50  

        self.angle_step = 270 / self.total_duration 


        self.create_loading_points()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(self.timer_interval)

        self.frame_count = 0

        self.show()

    def create_loading_points(self):
        self.loading_points = []
        for i in range(self.num_points):
            point = QGraphicsEllipseItem(-2.5, -2.5, 5, 5)  
            point.setBrush(QColor(255, 255, 255))

            initial_angle = i * (360 / self.num_points)
            initial_position = QTransform().rotate(initial_angle).map(QPointF(self.radius, 0))

            point.setPos(initial_position)
            self.loading_points.append(point)
            self.scene.addItem(point)

    def update_animation(self):
  
        percentage = (self.frame_count * self.timer_interval / (self.total_duration * 1000)) * 100
        rotation = self.angle_step * (self.frame_count % int(self.total_duration * 1000 / self.timer_interval))
        for i, point in enumerate(self.loading_points):
            angle = rotation + i * (self.angle_step / (self.num_points - 1))
            transform = QTransform().rotate(angle)
            rotated_point = transform.map(QPointF(self.radius, 0))
            point.setPos(rotated_point)

        self.frame_count += 1

        # Si le chargement atteint 100%, lancer le code Navigation.py
        if percentage >= 100 and self.frame_count >= int(self.total_duration * 1000 / self.timer_interval):
            self.timer.stop()  
            self.close()  
            self.loading_completed.emit()

############################################################
############################################################
############################################################
# Test : Les test pour l'interface utilisateur se feront en constatant
        #visuellement si les actions sont effectuées. Les test suivants doivent 
        #être réalisés.
# - 1 : La fenêtre affiche correctement l'animation (points qui tournent au centre de la page)      
############################################################
############################################################
############################################################
                  

def display_test():
    
    app = QApplication(sys.argv)
    fenetre = LoadingScreen()
    fenetre.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    test = input("Tester les fonctions du script ? (0/1) : ")
    if test : display_test()
