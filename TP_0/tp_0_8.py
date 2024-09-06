# On créé une fonction pour effectuer le calcul demandé
def f(x):
    try:
        return pow(x, 2) / (1 + x)
    except ZeroDivisionError:
        print("f n'est pas definie pour x=-1.")

print("y=" + str(f(-1)))