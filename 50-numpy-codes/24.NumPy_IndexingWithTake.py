# Indexing with np.take
import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Using np.take to select elements at specific indices
indices = [0, 2, 4]
result = np.take(array, indices)

# don't need take function . i can u it just slicing
print('Selected Elements using np.take:', result)
print(array[0::2])