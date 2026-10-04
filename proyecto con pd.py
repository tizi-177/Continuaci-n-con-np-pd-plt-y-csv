import pandas as pd

data = {
    'nombre': ['Ana', 'Luis', 'Marta', 'Pedro', 'Sofía'],
    'edad': [23, 35, 29, 41, 27],
    'ciudad': ['Buenos Aires', 'Córdoba', 'Rosario', 'Mendoza', 'Buenos Aires'],
    'salario': [50000, 65000, 58000, 72000, 61000]
   
}
df = pd.DataFrame(data)


print(df.head(3))

print(df.info())

print(df.describe())

df.head(2)

print(df[df['edad'] > 28])

print(   df[df['ciudad'] != 'Buenos Aires'])

print(df[(df['salario'] > 55000) & (df['edad'] < 30)])

print(df.info())

print(df.sort_values('salario', ascending=False)) 

print(df.sort_values(['ciudad', 'edad']))

df['salario_anual'] = df['salario'].apply(lambda x: x * 12)

print(df[['nombre', 'salario', 'salario_anual']])

def categorizar_edad(edad):
    if edad < 30:
        return 'joven'
    else:
        return 'adulto'

df['categoria_edad'] = df['edad'].apply(categorizar_edad)

print(df[['nombre', 'edad', 'categoria_edad']])









