input = open("L1.txt")

siffror = "0123456789"
resultat = 0

for entry in input:
    siffra1 = -1
    siffra2 = -1
    hittadSiffra = False
    for tecken in entry:
        if tecken in siffror and hittadSiffra == False:
            siffra1 = int(tecken)
            hittadSiffra = True
        elif tecken in siffror: # will update for each new number found until end of entry
            siffra2 = int(tecken)
    if siffra2 == -1:
        #print(siffra1*11)
        resultat += int(siffra1*11)
    else:
        #print(siffra1*10+siffra2)
        resultat += siffra1*10+siffra2
print("Resultat:",resultat)