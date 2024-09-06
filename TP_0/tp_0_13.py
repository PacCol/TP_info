from random import randint

myList = []

# On créé une liste de nombre aléatoire netre 0 et 5.
for i in range(10):
    myList.append(randint(0, 5))

# On créé une fonction pour effectuer les calculs demandés
def f(x):
    results = []
    for i in x:
        try:
            results.append(pow(i, 2) / (1 + i))
        except ZeroDivisionError:
            print("f n'est pas definie pour x=-1.")
            results.append(None)
    return results

# On affcihe les résultats
print("Pour les valeurs de la liste:")
print(myList)
print("On obtient les images par f:")
print(f(myList))