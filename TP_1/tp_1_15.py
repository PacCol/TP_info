def comptage_dico(L):
    dico = {}
    for i in L:
        dico[i] = L.count(i)
    return dico

L = [7, 3, 10, 3, 7, 4, 0, 3245, 56, 2]
L1= []

dico = comptage_dico(L)

for i in dico:
    for j in range(dico[i]):
        L1.append(i)

print(L1)