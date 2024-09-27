from random import randint

L = []
for i in range(20):
    L.append(randint(1, 10))

print(L)
print("4 appears " + str(L.count(4)) + " time(s) in the list.")