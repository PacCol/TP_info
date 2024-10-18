try:
    f = open("test.txt", "r")
except:
    print("Impossible d'ouvir le fichier, car il est impossible de trouver un fichier test.txt dans le dossier de travail.")
f = open("Fichiers/test.txt", "r")
f.close()