import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("WindowsPowerShell/ventas_techstore.csv")


#1)Agregá al DataFrame una columna "total" = cantidad * precio_unitario
# y devolvé el DataFrame con esa columna nueva.
def agregar_columna_total(df):
    df["total"] = df["cantidad"] * df["precio_unitario"]
    
    return df
    


#2)Devolvé una Serie (o DataFrame) con el total vendido ($) por producto,
# ordenado de mayor a menor.
# Tip: groupby("producto")["total"].sum().sort_values(ascending=False)

def ventas_por_producto(df):
    resultado = df.groupby("producto")["total"].sum()
    resultado = resultado.sort_values(ascending=False)
   
    return resultado

#3)Devolvé un DataFrame con, por cada vendedor: total vendido y
# cantidad de operaciones (filas) que realizó.
# Tip: groupby("vendedor").agg(total=("total","sum"), operaciones=("total","count"))

def rendimiento_por_vendedor(df):
    resultado = df.groupby("vendedor").agg(
        total=("total", "sum"),
        operaciones=("total", "count")
    )
    
    return resultado

#4)Devolvé solo las filas de la región "Norte" donde el total
# vendido en esa operación haya sido mayor a $50.000.

def ventas_norte_altas(df):
    resultado = df[(df["region"] == "Norte") & (df["total"] > 50000)]
    
    return resultado

#5)Creá una tabla pivot con categorías como filas, regiones como
# columnas, y el total vendido como valores.
# Tip: pd.pivot_table(df, index="categoria", columns="region", values="total", aggfunc="sum", fill_value=0)

def pivot_categoria_region(df):
    
    return pd.pivot_table(df, values = "total", index = "categoria", columns = "region", aggfunc = np.sum, fill_value = 0)

#6)Devolvé un diccionario con:
# - "mejor_dia": la fecha (str) con mayor total vendido
# - "monto_mejor_dia": el monto de ese día
# - "promedio_diario": el promedio de ventas totales por día

def resumen_diario(df):
    df["fecha"] = pd.to_datetime(df["fecha"])
    mejor_dia = df.groupby("fecha")["total"].sum().idxmax().strftime("%Y-%m-%d")
    
    monto_mejor_dia = df.groupby("fecha")["total"].sum().max()
    
    promedio_diario = df.groupby("fecha")["total"].sum().mean()
    
    nombres_clave = {"mejor_dia": mejor_dia, "monto_mejor_dia": monto_mejor_dia, "promedio_diario": promedio_diario}
    
    return nombres_clave



df.info()

df.describe()





