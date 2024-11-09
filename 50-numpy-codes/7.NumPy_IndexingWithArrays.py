# NumPy - Indexing with Arrays
import numpy as np
# Creating a 2D array
array_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Create a 3D array
array_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])

# Using arrays for indexing
rows = np.array([0, 1, 2])
cols = np.array([2, 1, 0])
indexed_elements = array_2d[rows, cols]
# print('Indexed Elements:', indexed_elements)

# using for 3d . try it next time again for better understanding
row = np.array([[0,1,1]])
row = array_3d[row]
print(row)
