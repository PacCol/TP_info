f = open("Fichiers/tableau.csv", "r")

col1 = []
col2 = []
content = f.read().split("\n")

for i in content:
    col1.append(i.split(";")[0])
    col2.append(i.split(";")[1])

print("Column 1: " + str(col1))
print("Column 2: " + str(col2))