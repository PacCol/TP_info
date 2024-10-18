from random import randint

liste = []
images = []

for i in range(-100, 100, 2):
    liste.append(i/100)

for i in liste:
    images.append((1-i**2)**(1/2))

f = open("Fichiers/tableau2.csv", "w")

for i in range(len(liste)):
    f.writelines(str(liste[i]) + "; " + str(images[i]) + "\n")

f.close()