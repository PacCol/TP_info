from random import randint
from time import perf_counter

def trie_bulles(liste_a_trier):
    for j in range(len(maListe)):
        for i in range(len(liste_a_trier)-1):
            if liste_a_trier[i] > liste_a_trier[i+1]:
                a = liste_a_trier[i]
                liste_a_trier[i] = liste_a_trier[i+1]
                liste_a_trier[i+1] = a
    return liste_a_trier

for i in [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240]:
    maListe = []
    for j in range(i):
        maListe.append(randint(-10000, 10000))
    t1 = perf_counter()
    liste_triee = trie_bulles(maListe)
    maListe.sort()
    print("Temps écoulé pour une liste de " + str(i) + " éléments: " + str(perf_counter() - t1) + "s")
    if liste_triee == maListe:
        print("La liste a bien été triée.")
    else:
        print("Erreur...")
