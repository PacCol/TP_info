def remplacer(L, a, b):
    for i in range(len(L)):
        if L[i] == a:
            L[i] = b
    return(L)

L1 = [8, 7, 6, 8, 2, 8]
print("Dans la liste " + str(L1) + ", on remplace les 8 par des 100, on obtient:")
L2 = remplacer(L1, 8, 100)
print(L2)