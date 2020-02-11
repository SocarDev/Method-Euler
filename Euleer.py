import matplotlib.pyplot as plt
import numpy as np


def function(q, w):
    ec = (2 * q) * ((w - 1) ** (1 / 2))  # Here you define your differential equation..
    return ec


h = float(input("Tamaño de paso: "))
s = float(input("¿Hasta que valor?: "))
n = int(s / h) + 1
x = [0, 0]
y = [0, 0]
for i in np.arange(1, n):
    y[i] = y[i - 1] + (function(x[i - 1], y[i - 1])) * h
    y.append(y[i])
    x[i] = x[i - 1] + h
    x.append(x[i])
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Método de Euler.')
plt.show()
