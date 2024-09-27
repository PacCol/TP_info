def maximum(L):
    a = L[0]
    for i in range(len(L)):
        if L[i] > a:
            a = L[i]
    return a

print("La valeur la plus élévée de la liste [1, 7, 9, 54, 1] est: " + str(maximum([1, 7, 9, 54, 1])))