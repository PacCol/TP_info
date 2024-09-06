# On définit une fonction f quelquconque.
def f(x):
    return 2*pow(x, 2)

# On calcule le taux d'accroissement.
def dérivée_f(x, incrément):
    return((f(x + incrément) - f(x)) / incrément)

# On calcule la primitive
def intégrale_f(a, b, incrément):
    intégrale = 0
    for i in range(int((b-a)/incrément)):
        intégrale+= f(a + i*incrément)*incrément
    return intégrale

print("Dans notre cas f(x)=2x²")
print("Dérivé de f en 3: " + str(dérivée_f(3, 0.0001)))
print("Intégrale de f de 3 à 8: " + str(intégrale_f(3, 8, 0.00001)))