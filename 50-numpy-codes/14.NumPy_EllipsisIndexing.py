# NumPy - Using Ellipsis (...) in Indexing
import numpy as np

# Creating a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# Using ellipsis to select all elements along specific axes
result3d = array_3d[..., 1]  # Selecting the second column in each 2D slice
print('Result using Ellipsis of 3D (...):\n', result3d)
# 2D array
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# create a 1D array using 2D array 2no columns value
result2d = array_2d[...,2]
print('Result using Ellipsis of 2D (...):\n', result2d)

# It's totally different
result2d = array_2d[2,...]
print('Result using Ellipsis of 2D (...):\n', result2d)