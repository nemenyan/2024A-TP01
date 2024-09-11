# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est votre nom?")
date = input("Quelle est la date du record?")
discipline = input("Quelle est la discipline de l'athlète?")
categorie = input("Dans quelle catégorie est l'athlète?")
record = input("Combien de temps était le record?")

resultat = ("Nouveau Record : " + "\n" + "---------" + "\n" + str(date) + "\n" + str(discipline) + " - " + str(categorie) + "\n" + str(athlete) + " " + str(country) + " - " + str(record) )
print(resultat)