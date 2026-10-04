import matplotlib.pyplot as plt
import numpy as np

datos = np.random.randn(1000)

plt.hist(datos, bins=30, color="skyblue", edgecolor="black")
plt.title("Distribución de datos")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()