# NumPy - Multi-dimensional Array Indexing with Mixed Types
import numpy as np

# Creating a 3D array: 1 no row to last, then 0 no row then every row 1 no clumn
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# Mixing slicing with direct indexing
mixed_index = array_3d[1:, 0, 1]

print('Mixed Type Indexing Result:', mixed_index)

# every row the 1 no row then 1 no columns values
print(f'Mixed Indexing: {array_3d[0:,1,1]}')