def trouver_minimum(L):
    minimum = L[0]
    minimiseur = 0
    for i in range(len(L)):
        if L[i] <= minimum:
            minimum = L[i]
            minimiseur = i
    return minimum, minimiseur

print("La valeur la moins élévée de la liste [1, 7, 9, 54, 1] est " + str(trouver_minimum([1, 7, 9, 54, 1])[0]) + " et se situe au rang " + str(trouver_minimum([1, 7, 9, 54, 1])[1]))