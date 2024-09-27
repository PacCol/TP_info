L = [1, 56, 87, 35, 56, 12, 0, 7, 12]

def comptage_dico(L):
    dico = {}
    for i in L:
        dico[i] = L.count(i)
    return dico

def tri_comptage(L):
    L1 = []
    dico = comptage_dico(L)

    for k in range(len(dico)):
        minimum = 23456789876543234567898765432
        for i in dico:
            if i < minimum:
                minimum = i
        for i in range(dico[i]):
            L1.append(minimum)
        del dico[minimum]
    return L1

print(tri_comptage(L))

