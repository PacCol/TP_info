L = [7, 3, 10, 3, 7, 4, 0, 3245, 56, 2]

def comptage_dico(L):
    dico = {}
    for i in L:
        dico[i] = L.count(i)
    return dico

print(comptage_dico(L))