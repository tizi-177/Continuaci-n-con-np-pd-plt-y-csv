import numpy as np

arr = np.random.randint(0, 100, size=(3, 4))

np.shape(arr)

print(arr.reshape(4, 3))

arr = arr.flatten()

arr = arr.reshape(-1)

print(arr)















