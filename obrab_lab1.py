import numpy as np
import matplotlib.pyplot as plt
with open('tutorial.txt', 'r') as file:
    t = file.readlines()
c, g = '', ''
l, s, a, b = [], [], [], []
d, e = 0.06, 0.01
for i in range(499):
    a.append(int(t[i][:-1]))
for i in range(499, 998):
    b.append(float(t[i][:-1]))

x = np.array(a)
y = np.array(b)

plt.errorbar(x, y,  xerr = 0, yerr = 0, fmt='o')
plt.grid()
plt.ylabel('$T, c$')
plt.xlabel('$N, эл$')
plt.title("Зависимость времени работы программы от размера массива")
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()
