from random import randint

myList = []

for i in range(10):
    myList.append(randint(0, 100))

# On affcihe le troisième élément
print("Le troisième élement de la liste est " + str(myList[2]) + ".")

#On affcihe la liste entière
print("La liste entière est " + str(myList) + ".")
