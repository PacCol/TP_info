from random import randint

liste = []
images = []

for i in range(100):
    liste.append(randint(-100, 100)/100)

for i in liste:
    images.append((1-i**2)**(1/2))

print("L'image de " + str(liste[0]) + " est " + str(images[0]) + ".")
print("L'image de " + str(liste[-1]) + " est " + str(images[-1]) + ".")