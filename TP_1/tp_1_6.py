# On affiche chaque élément de la liste un par un.
def afficher_liste(L):
    for i in range(len(L)):
        x=L[i]
        print(x, end=" ") 
    print("")

afficher_liste([1,7,8,3,18,24,12,0,3])

# On affiche chaque élément de la liste un par un.
def afficher_liste1(L):
    i = 0
    while i < len(L):
        x=L[i]
        print(x, end=" ")
        i+=1
    print("")

afficher_liste1([1,7,8,3,18,24,12,0,3]) 