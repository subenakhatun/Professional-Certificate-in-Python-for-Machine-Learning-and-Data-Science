# NumPy - Masked Indexing
import numpy as np

# Creating an array
array = np.array([1, -2, 3, -4, 5])

# Creating a mask for positive values
mask = array > 4

# Applying mask to get only positive values
positive_values = array[mask]

print('Positive Values:', positive_values)

array_1 = np.array([[1, 2, 3],[4, 5, 6]])
array_2 = np.array([[4, 5, 6],[10, 12, 14]])
postive = array_1 > 4 
print(array_1[postive])
