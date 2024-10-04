maListe = [1, 7, 9, 3, 2, 10, 4, 17, 4567, 34, 12, 56, 778, 417, 0, 12]

def trie_bulles(liste_a_trier):
    for j in range(len(maListe)):
        for i in range(len(liste_a_trier)-1):
            if liste_a_trier[i] > liste_a_trier[i+1]:
                a = liste_a_trier[i]
                liste_a_trier[i] = liste_a_trier[i+1]
                liste_a_trier[i+1] = a
    return liste_a_trier

print(trier_liste(maListe))