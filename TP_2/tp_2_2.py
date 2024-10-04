import itertools

n = 4
m = 5

for i,j in itertools.product(range(n), range(m)):
    print("(" + str(i) + ", " + str(j) + ")\n")