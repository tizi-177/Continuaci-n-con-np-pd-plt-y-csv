import matplotlib.pyplot as plt

meses = ["Ene", "Feb", "Mar", "Abr", "May"]
ventas = [120, 150, 90, 200, 170]

plt.bar(meses, ventas, color=["orange", "blue", "green", "red", "purple"])
plt.title("Ventas mensuales")
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.show()
























