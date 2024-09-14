#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")
dor = 0
argent=0
bronze=0
for i in code_medals:
 if i not in ["G","S", "B"]: #commande marche pas
    print("Ceci est une chaine invalide")
    code_medals = input ("Quelle est la chaine de caractères représentant le résultat du pays?")

dor = code_medals.count('G')
argent = code_medals.count('S')
bronze = code_medals.count('B')
resultat = str(country) + ":" + "\n" + "- " + str(dor) + " OR" + "\n" + "- " + str(argent) + " Argent" + "\n" + "- " + str(bronze) + " Bronze"
print(resultat)
