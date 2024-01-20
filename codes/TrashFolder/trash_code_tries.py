def trouver_elements(liste, str_recherche):
    return [element for element in liste if str_recherche in element]

# Exemple d'utilisation
ma_liste = ["Unnamed 0.1", "chien", "oiseau", "chaton", "chiot"]
str_recherche = "Unnamed"
resultat = trouver_elements(ma_liste, str_recherche)
print(resultat)
