from random import randint

L = []
for i in range(20):
    L.append(randint(1, 10))

print(L)
print("The " + str(L.index(4) + 1) + " element is a 4.")
L.remove(10)
print("Without 10: " + str(L))