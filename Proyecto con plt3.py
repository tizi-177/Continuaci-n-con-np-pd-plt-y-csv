import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color="purple")
plt.title("Puntos aleatorios")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()