# NumPy - Flattening a Multi-dimensional Array
import numpy as np

# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
# The . flatten() function in NumPy is a powerful tool for reshaping multi-dimensional arrays into one-dimensional arrays.
# Flattening the array
flattened_array = array_2d.flatten()

print('Flattened Array:', flattened_array)
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
flattened_array = array_3d.flatten()

print('Flattened Array:', flattened_array)