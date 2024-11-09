# NumPy - Multi-dimensional Slicing
import numpy as np
array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
# Multi-dimensional slicing
print(array_2d[1:, 1:3]) # 1st row to last row, 1 colum to 3 colums
print(array_2d[:, 1:3])
print(array_2d[2, :3])