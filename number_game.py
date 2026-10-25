import random

secret = random.randint(1, 100)
devine = 0
essais = 0
essaismax = 10

while devine != secret:
    try:
        devine = int(input("Devine le nombre : "))
    except ValueError:
        print("Entre un nombre valide !")
        continue

    essais += 1

    if devine < secret:
        print(devine, "est plus petit que le nombre.")
    elif devine > secret:
        print(devine, "est plus grand que le nombre.")
    else:
        break  # trouvé : on sort de la boucle

    print("Il vous reste", essaismax - essais, "essais.")
    if essais == essaismax:
        print("Vous avez perdu ! Le nombre était", secret)
        break

if devine == secret:
    if essais <= 7:
        print("Bravo, trouvé en", essais, "essais, moins de 7 !")
    else:
        print("Bravo, vous avez trouvé", secret, "en", essais, "essais !")