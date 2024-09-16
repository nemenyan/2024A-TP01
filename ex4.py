# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Pourcentage de batterie: "))
if battery_level == 0:
    print("La batterie est vide")
else:
     if battery_level >=50 :
        a = (battery_level- 50)
        b = (battery_level- a )-25 
        c = (battery_level- a - b)- 10
        d = (battery_level- a - b - c) - 5
        e = (battery_level - a-b-c) - 5
        distance = round((a*2)+(b*0.5)+(c*1)+(d*2.5)+(e*6),1)
        print(f"La distance possible est de: {distance}km")

     elif 25 <= battery_level <50:
         b = (battery_level-25) 
         c = (battery_level - b)- 10
         d = (battery_level- b - c) - 5
         e = (battery_level- b-c) - 5
         distance = round((b*0.5)+(c*1)+(d*2.5)+(e*6),1)
         print(f"La distance possible est de: {distance}km")

     elif 10 <= battery_level < 25:
         c = (battery_level- 10)
         d = (battery_level- c) - 5
         e = (battery_level- c) - 5
         distance = round((c*1)+(d*2.5)+(e*6),1)
         print(f"La distance possible est de: {distance}km")

     elif 5 <= battery_level < 10:
         d = (battery_level- 5)
         e = (battery_level- 5)
         distance = round((d*2.5)+(e*6),1)
         print(f"La distance possible est de: {distance}km")
  
     elif  battery_level < 5 :
      e = (battery_level+5)
      distance = round((e*6),1)
      print(f"La distance possible est de: {distance}km")
