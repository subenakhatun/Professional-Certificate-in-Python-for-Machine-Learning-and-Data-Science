# NumPy - Indexing with np.where()
import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Using np.where to find indices where elements are greater than 25. not that much necessary . cz we can use it as simple
indices = np.where(array > 25)
# where just use por index position number
print('Indices where elements > 25:', indices)
print('Values where elements > 25:', array[indices])
values = array > 25
print(array[values])
