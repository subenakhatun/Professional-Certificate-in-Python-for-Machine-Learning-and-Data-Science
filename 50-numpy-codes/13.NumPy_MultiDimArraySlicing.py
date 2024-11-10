# NumPy - Indexing Multi-dimensional Arrays with Slices
import numpy as np
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# first cols then rows
print(array_2d[1:, :2])
print(array_2d[0:, :2])