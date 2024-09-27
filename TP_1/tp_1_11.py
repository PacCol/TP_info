def maxi_maxi(L):
    maximum1 = L[0]
    maximum2 = L[1]
    for i in range(len(L)):
        if L[i] > maximum1:
            maximum1 = L[i]
    for i in range(len(L)):
        if maximum2 <= L[i] < maximum1:
            maximum2 = L[i]
    return maximum1, maximum2

print("Les valeurs les plus élévées de la liste [1, 7, 9, 54, 1, 54] sont " + str(maxi_maxi([1, 7, 9, 54, 1, 54])[0]) + " et " + str(maxi_maxi([1, 7, 9, 54, 1, 54])[1]) + ".")