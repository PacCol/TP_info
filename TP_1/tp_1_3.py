from random import randint

L = []
for i in range(20):
    L.append(randint(1, 10))

L.sort()
print(L)

L.sort(reverse=True)
print(L)