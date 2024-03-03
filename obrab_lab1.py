import numpy as np
import matplotlib.pyplot as plt
with open('tutorial.txt', 'r') as file:
    t = file.readlines()
a, b = [], []
for i in range(50):
    a.append(int(t[i].split()[0]))
for i in range(50):
    b.append(float(t[i].split()[1]))

x1 = np.array(range(1000, 11000, 200))
x2 = np.array(range(1000, 11000, 200))
y1 = np.array(a)
y2 = np.array(b)

plt.errorbar(x1, y1,  xerr = 0, yerr = 0, fmt='o', color='b')
plt.errorbar(x2, y2,  xerr = 0, yerr = 0, fmt='o', color='r')
plt.grid()
plt.ylabel('$T, c$')
plt.xlabel('$N, эл$')
plt.title("Зависимость времени работы программы от размера массива")
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()
