import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as path_effects
# Génération de données aléatoires pour l'exemple
data = np.random.randn(1000)

# Préparation de la figure
plt.figure(figsize=(10, 6))
bins = 30

# Création de l'histogramme avec ombres
n, bins, patches = plt.hist(data, bins=bins, color='#4169e1', edgecolor='black', alpha=0.7)
import matplotlib.pyplot as plt
import numpy as np

# Génération de données aléatoires pour l'exemple
data = np.random.randn(1000)



# Application d'un motif pour simuler l'aspect du bois
for patch in patches:
    patch.set_facecolor('#8B4513')  # Couleur marron foncé pour le bois
    patch.set_hatch('///')  # Motif pour imiter la texture du bois



# Ajout d'ombres pour chaque barre
for patch in patches:
    x = patch.get_x() + patch.get_width() / 2
    y = patch.get_height()
    plt.text(x, y, f'{int(y)}', ha='center', va='bottom', fontweight='bold', color='black')

    # Création de l'effet d'ombre
    patch.set_edgecolor('white')
    patch.set_linewidth(0.8)
    patch.set_path_effects([path_effects.withStroke(linewidth=3, foreground='black')])

# Personnalisation de la figure
plt.gca().set_facecolor('#f5f5f5')  # Couleur de fond
plt.title("Histogramme Avancé - Style Professionnel", fontsize=18, fontweight='bold')
plt.xlabel("Valeurs", fontsize=14, fontweight='bold')
plt.ylabel("Fréquence", fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Affichage de l'histogramme
plt.show()
