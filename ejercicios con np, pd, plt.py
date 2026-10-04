import numpy as np

import pandas as pd

import matplotlib.pyplot as plt



Notas = {
    
    'Alumnos' : ['Ana', 'Luis', 'Marta', 'Pedro', 'Sofia', 'Juan'],
    
    'Examen1' : [np.random.randint(0, 100) for i in range(6)],
    
    'Examen2' : [np.random.randint(0, 100) for i in range(6)],
    
    'Examen3' : [np.random.randint(0, 100) for i in range(6)],
    
    'Examen4' : [np.random.randint(0, 100) for i in range(6)]
}

df = pd.DataFrame(Notas)


Promedio = (df['Examen1'] + df['Examen2'] + df['Examen3'] + df['Examen4']) / 4

df['promedio'] = Promedio

plt.title('Promedios de los alumnos')

plt.bar(df['Alumnos'], df['promedio'], color='blue')

plt.xlabel('Alumnos')

plt.ylabel('Promedio')

plt.show()



















