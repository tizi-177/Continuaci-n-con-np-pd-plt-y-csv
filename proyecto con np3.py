import numpy as np

matriz = np.array([[5, 5], [5, 5]])

n = matriz.shape[0]
k = -1
filas = np.arange(-k, n)
columnas = np.arange(0, n + k)

matriz[filas, columnas] = 0

print(matriz)





