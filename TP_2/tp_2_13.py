from random import randint
from time import perf_counter

def comptage_dico(L):
    dico = {}
    for i in L:
        dico[i] = L.count(i)
    return dico

def tri_comptage(L):
    L1 = []
    dico = comptage_dico(L)

    for k in range(len(dico)):
        minimum = 10000
        for i in dico:
            if i < minimum:
                minimum = i
        for i in range(dico[i]):
            L1.append(minimum)
        del dico[minimum]
    return L1

for i in [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240]:
    maListe = []
    for j in range(i):
        maListe.append(randint(-10000, 10000))
    t1 = perf_counter()
    liste_triee = tri_comptage(maListe)
    print(liste_triee)
    maListe.sort()
    print("Temps écoulé pour une liste de " + str(i) + " éléments: " + str(perf_counter() - t1) + "s")
    if liste_triee == maListe:
        print("La liste a bien été triée.")
    else:
        print("Erreur...")