import time
import keyboard
Horloge = [16, 25, 8]
seconde = 0
tupleTime = (int(input("Nouvelle heure:")), int(input("Nouvelles minutes:")), int(input("Nouvelles secondes:")))
alarmeTuple = (int(input("Heure de l'alarme:")), int(input("Minutes de l'alarme:")), int(input("Secondes de l'alarme:")))
choice = int(input("1.Choisir le format d'affichage 24 heures.\n2.Choisir le format d'affichage 12 heures:\n"))
continuer = True
# Essai de pour aller plus loin deuxième partie
#Il faut rester appuyer sur "s" afin de stopper l'horloge
def stop_horloge():
    global continuer
    if keyboard.is_pressed("s"):
        continuer = False
    
        
#Il faut rester appuyer sur "c" afin de remettre en marche l'horloge

def remettre_en_marche_horloge():
    global continuer
    if keyboard.is_pressed("c"):
        continuer = True
        


# Essai de pour aller plus loin première partie 

def format_heure(choice):
    if choice == 1:
        print(f"Heure: {Horloge[0]:02}:{Horloge[1]:02}:{Horloge[2]:02}")
    elif choice == 2:
        if Horloge[0] <= 12 and Horloge[1] <= 59 and Horloge[2] <= 59:
            print(f"Heure: {Horloge[0]:02}:{Horloge[1]:02}:{Horloge[2]:02} AM")
        elif Horloge[0] > 12:
            print(f"Heure: {Horloge[0]-12:02}:{Horloge[1]:02}:{Horloge[2]:02} PM")


# Deuxième partie de l'exercice, fonction avec tuple
# qui permet de changer l'heure affichée

def afficher_heure(tupleTime):
    if tupleTime[0] < 24 and tupleTime[0] >= 0 and tupleTime[1] < 60 and tupleTime[1] >= 0 and tupleTime[2] < 60 and tupleTime[2] >= 0:
        Horloge[0] = tupleTime[0]
        Horloge[1] = tupleTime[1]
        Horloge[2] = tupleTime[2]
        return Horloge[0], Horloge[1], Horloge[2]
    else:
        print("Cette nouvelle heure ne peut pas être entrée")

afficher_heure(tupleTime)

# Troisième partie de l'exercice, heure à laquelle
# l'alarme sonne

def alarme(alarmeTuple):
     if alarmeTuple[0] == Horloge[0] and alarmeTuple[1] == Horloge[1] and alarmeTuple[2] == Horloge[2]:
            print("DRRRRRRRRINNNNNNNNG")
    
# Première partie de l'exercice, heure que l'on doit 
# arrêter en fermant le programme.
#Le premier while True et if continuer == True ont été rajouté pour le pour aller plus loin partie deux

while True:
    if continuer == True:
        while True:
            for i in Horloge: 
                while Horloge[2] < 60 and Horloge[1] < 60 and Horloge[0] < 24 and continuer == True:
                    Horloge[2] += 1
                    #pour aller plus loin partie deux
                    stop_horloge()
                    if Horloge[2] == 60 and Horloge[1] < 60  and Horloge[0] < 24:
                        Horloge[1] += 1
                        Horloge[2] = 0
                        if Horloge[2] == 0 and Horloge[1] > 59 and Horloge[0] < 24:
                            Horloge[0] += 1
                            Horloge[1] = 0
                            if Horloge[0] == 24 and Horloge[1] == 0  and Horloge[2] == 0:
                                Horloge[0] = 0
                    time.sleep(1)
                    format_heure(choice)
                    # Partie alarme 
                    alarme(alarmeTuple)
                else:
                    remettre_en_marche_horloge()