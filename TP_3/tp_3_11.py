import matplotlib.pyplot as plt

col1 = []
col2 = []

f = open("Fichiers/tableau2.csv")
content = f.read().split("\n")
print(content)
f.close()

for i in content:
    try:
        col2.append(float(i.split(";")[1]))
        col1.append(float(i.split(";")[0]))
    except:
        pass

plt.figure("Graph")
plt.plot(col1, col2)
plt.show()