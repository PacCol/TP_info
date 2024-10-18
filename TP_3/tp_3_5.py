f = open("Fichiers/test.txt", "r")

# On affiche les caractères 3 par 3.
for i in range(3):
    print(f.read(3))

# On revient au début du fichier.
f.seek(0)

# On affiche la première ligne.
print(f.readline())