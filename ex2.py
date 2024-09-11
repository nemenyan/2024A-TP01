# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity =int (input("Veuillez indiquer la quantité d'eau à assainir: "))
x= water_quantity
filtre= int(x/5)
UV_lamps= int(x *(3/5))
chlore = int(x *(0.5/5))
resultat=("Voici les matériaux requis pour l'assainissement de "+ str(water_quantity)+ "L d'eau:" + "\n" +"-"+ str(filtre)+ " filtres"+"\n"+"-"+ str(UV_lamps) + " lampes UV"+"\n"+"-"+ str(chlore)+ " kg de chlore")
print(resultat)
