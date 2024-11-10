# NumPy - Splitting Arrays
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6])
array_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
# Splitting the array into three parts
split_arrays = np.array_split(array_3d, 5)

print('Split Arrays:', split_arrays)