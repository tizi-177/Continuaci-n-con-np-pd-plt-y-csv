import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
cuadrados = [n**2 for n in x]
cubos = [n**3 for n in x]

plt.plot(x, cuadrados, color="green", marker="o", label="x²")
plt.plot(x, cubos, color="blue", marker="s", label="x³")

plt.title("Cuadrados vs Cubos")
plt.xlabel("Números")
plt.ylabel("Resultado")
plt.legend()
plt.show()












