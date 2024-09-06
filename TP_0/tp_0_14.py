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

def antécédents_de_f(image_par_f, borne_inf, borne_sup, incrément):
    # On créé la liste de nombre entre leqsquels chercher l'antécédent
    myList = []
    for i in range(int((borne_sup-borne_inf)/incrément)):
        myList.append(borne_inf + incrément*i)
    results = f(myList)
    # On cherche les images qui correpondent à x
    encadrements = []
    for i in range(0, len(results)):
        try:
            if results [i] < image_par_f < results[i+1]:
                encadrements.append([myList[i - 1], myList[i + 1]])
        except:
            print("L'image qu'on test n'existe pas, on passe...")
    return encadrements

# On affiche les résultats
x = 2.8269
antécédents = antécédents_de_f(x, 3, 4, 0.0000001)
print("L'antécédent positif de " + str(x) + " par f est dans l' encadrement: " + str(antécédents[0]))
print("La calculatrice donne comme valeur 3.61.")
