from random import randint

myList = []
myResults = []

# On créé une liste de nombre aléatoire netre 0 et 5.
for i in range(10):
    myList.append(randint(0, 5))

# On créé une fonction pour effectuer le calcul demandé
def f(x):
    try:
        return pow(x, 2) / (1 + x)
    except ZeroDivisionError:
        print("f n'est pas definie pour x=-1.")

# On calcule les images
for i in range(10):
    myResults.append(f(myList[i]))

# On affcihe les résultats
for i in range(10):
    print("Pour x=" + str(myList[i]) + ", f(x)=" + str(myResults[i]) + ".")