import matplotlib.pyplot as plt

col1 = []
col2 = []

def lecture_donnee(chemin):

    try:
        if chemin.split(".")[-1] != "csv":
            return
    except:
        return

    f = open(chemin, "r")
    content = f.read().split("\n")
    f.close()

    for i in content:
        if ";" in i:
            try:
                col1.append(float(i.split(";")[0]))
                try:
                    col2.append(float(i.split(";")[1]))
                except:
                    col2.append(0)
            except:
                pass

    plt.figure("Graph")
    plt.plot(col1, col2)
    plt.show()

lecture_donnee("Fichiers/tableau2.csv")