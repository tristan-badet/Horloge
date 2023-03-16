import time
Horloge = [16, 25, 8]
seconde = 0

while True:
    
    for i in Horloge: 
        while Horloge[2] < 60 and Horloge[1] < 60 and Horloge[0] < 24:
            Horloge[2] += 1
            if Horloge[2] == 60 and Horloge[1] < 60  and Horloge[0] < 24:
                Horloge[1] += 1
                Horloge[2] = 0
                if Horloge[2] == 0 and Horloge[1] > 59 and Horloge[0] < 24:
                    Horloge[0] += 1
                    Horloge[1] = 0
                    if Horloge[0] == 24 and Horloge[1] == 0  and Horloge[2] == 0:
                        Horloge[0] = 0
            time.sleep(1)
            print(Horloge[0], Horloge[1], Horloge[2])       