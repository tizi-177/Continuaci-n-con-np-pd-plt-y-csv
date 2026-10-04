import numpy as np

#Reemplazo de valores aleatorios

arr = np.array([5, np.nan, 8, np.nan, np.nan, 12, 20])

arr[np.where(np.isnan(arr))] = np.random.choice(np.arange(1, 100), size = np.sum(np.isnan(arr)))


print("Valores reeplazados por números aleatorios:", arr)

















