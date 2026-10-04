from os import rename

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("WindowsPowerShell/ventas_techstore.csv")

#1) Uní ventas con vendedores usando la columna en común "vendedor".
# Tip: pensá qué tipo de "join" necesitás si querés conservar TODAS
# las ventas, tengan o no un vendedor que matchee en la otra tabla.

def unir_ventas_y_vendedores(ventas, vendedores):
   return ventas.join(vendedores.set_index("vendedor"), on="vendedor", how="left") 

#2) A partir del DataFrame combinado, agregá una columna "dia_semana"
# con el nombre del día (lunes, martes, etc. o en inglés está bien).
# Tip: una columna datetime tiene un accesor especial para estas cosas.
def agregar_dia_semana(df):
 df["fecha"] = pd.to_datetime(df["fecha"])
 df["dia_semana"] = df["fecha"].dt.day_name()
 return df

#3)Devolvé el total vendido agrupado por "dia_semana".
def ventas_por_dia_semana(df):
    resultado = df.groupby("dia_semana")["total"].sum()
    resultado = resultado.sort_values(ascending=False)
    return resultado

#4)Para cada vendedor, calculá cuánto vendió en total y compará
# contra su "meta_mensual". Devolvé un DataFrame con columnas:
# vendedor, total_vendido, meta_mensual, cumplio (True/False)
def cumplimiento_meta(df):
    resultado = df.groupby("vendedor")["total"].sum().reset_index().rename(columns = {"total":"total_vendido"})
    resultado = resultado.merge(df[["vendedor", "meta_mensual"]].drop_duplicates(), on="vendedor")
    resultado["cumplio"] = resultado["total_vendido"] >= resultado["meta_mensual"]
    return resultado

#5) Graficá un gráfico de barras con el total vendido por vendedor.
# No hace falta devolver nada: la función debe mostrar el gráfico.
# Tip: podés armar primero la Serie con el total por vendedor,
# y después buscar cómo graficar una Serie directamente,
# o usar las funciones de matplotlib (plt.bar, plt.show).
def graficar_ventas_por_vendedor(df):
    total_por_vendedor = df.groupby("vendedor")["total"].sum()
    total_por_vendedor.plot(kind="bar")
    plt.xlabel("Vendedor")
    plt.ylabel("Total Vendido")
    plt.title("Ventas por Vendedor")
    plt.show()
    
#6) Calculá cuántos días de antigüedad tiene cada vendedor
# (diferencia entre hoy y "fecha_ingreso"), y devolvé un DataFrame
# con vendedor, antiguedad_dias y total_vendido, ordenado por
# antigüedad de mayor a menor.
# Tip: pd.Timestamp.today() te da la fecha de hoy; restar dos
# fechas datetime te da un objeto "Timedelta".
def antiguedad_y_ventas(df):
   df["fecha_ingreso"] = pd.to_datetime(df["fecha_ingreso"])
   df["antiguedad_dias"] = (pd.Timestamp.today() - df["fecha_ingreso"]).dt.days
   resultado = df.groupby("vendedor").agg(
       total_vendido=("total", "sum"),
       antiguedad_dias = ("antiguedad_dias", "first")
   )
   resultado = resultado.sort_values(by = "antiguedad_dias", ascending = False)
   return resultado.reset_index()[["vendedor", "antiguedad_dias", "total_vendido"]]
