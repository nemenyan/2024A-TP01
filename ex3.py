# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
import math

speed = float(input("Quelle est la vitesse initiale de la boule en m/s?"))
angle = float(input("Quel est l'angle de lancement en degrés?"))
g= 9.80
distance = (pow(speed,2) * math.sin(2*math.radians(angle)))/g
print(distance)
arrondid = round(distance,2)
print("La distance maximale en x est de ", arrondid,  " m")