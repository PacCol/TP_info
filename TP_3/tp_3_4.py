f = open("Fichiers/test.txt", "r")

for i in range(3):
    print(f.read(3))

# On affiche les caractères 3 par 3.