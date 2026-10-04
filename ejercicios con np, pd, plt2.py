import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)  # para que los resultados sean reproducibles

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Generamos las ventas de cada región, un valor por mes
Region1 = np.random.randint(0, 1000000, size=12)
Region2 = np.random.randint(0, 1000000, size=12)
Region3 = np.random.randint(0, 1000000, size=12)
Region4 = np.random.randint(0, 1000000, size=12)

# Armamos el DataFrame con los meses como índice
Puntuaciones_df = pd.DataFrame({
    'Region1': Region1,
    'Region2': Region2,
    'Region3': Region3,
    'Region4': Region4
}, index=meses)

print(Puntuaciones_df)

# Calculamos el total de cada región (suma de los 12 meses)
total1 = Puntuaciones_df['Region1'].sum()
total2 = Puntuaciones_df['Region2'].sum()
total3 = Puntuaciones_df['Region3'].sum()
total4 = Puntuaciones_df['Region4'].sum()

print("\nTotales por región:")
print(f"Region1: {total1}")
print(f"Region2: {total2}")
print(f"Region3: {total3}")
print(f"Region4: {total4}")

# Determinamos cuál región ganó comparando los totales numéricos
totales = {'Region1': total1, 'Region2': total2, 'Region3': total3, 'Region4': total4}
ganadora = max(totales, key=totales.get)
print(f"\nLa región ganadora es: {ganadora}")

# Posiciones en X para agrupar las barras (una al lado de la otra, no superpuestas)
x = np.arange(len(meses))
width = 0.2

plt.figure(figsize=(14, 6))

# Cada región se dibuja desplazada del centro, así no se tapan entre sí
for i, region in enumerate(['Region1', 'Region2', 'Region3', 'Region4']):
    offset = (i - 1.5) * width
    color = 'red' if region == ganadora else 'gray'
    plt.bar(x + offset, Puntuaciones_df[region], width, label=region, color=color)

plt.title(f'{ganadora} es la que más ha vendido')
plt.xlabel('Mes')
plt.ylabel('Ganancias')
plt.xticks(x, meses, rotation=45)  # acá se separan los nombres de los meses
plt.legend()
plt.tight_layout()
plt.savefig("ventas_regiones.png", dpi=120)
plt.show()






