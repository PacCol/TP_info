def nombre_occurences(L, a):
    count = 0
    for i in L:
        if i == a:
            count +=1
    return count

L = [1, 2, 6, 2]
print("Dans la liste [1, 2, 6, 2], 2 apparait " + str(nombre_occurences(L, 2)) + " fois.")