import numpy as np
import matplotlib.pyplot as plt
with open('tutorial.txt', 'r') as file:
    t = file.readlines()
a, b = [], []
for i in range(50):
    a.append(int(t[i].split()[0]))
for i in range(50):
    b.append(float(t[i].split()[1]))

x = np.array(a)
y = np.array(b)

plt.errorbar(x, y,  xerr = 0, yerr = 0, fmt='o', color='b')
plt.grid()
plt.ylabel('$T, c$')
plt.xlabel('$N, эл$')
plt.title("Зависимость времени работы программы от размера массива")
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()
