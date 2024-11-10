# NumPy - Concatenation of Arrays
import numpy as np

# Creating 1D arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Concatenating arrays: meand combine 2 arrays into 1 arrays
concatenated_array = np.concatenate((array1, array2))
array_add = array1+array2
print('Concatenated Array:', concatenated_array)
print('Concatenated Array using +:', array_add)

# creating 2D arrays
array_1 = np.array([[1, 2, 3],[4, 5, 6]])
array_2 = np.array([[4, 5, 6],[10, 12, 14]])
# array_concate_2d = np.concatenate(array_1,array_2)
# print(f'2d array concatinated: {array_concate_2d}')
# so at frist i need to convert it into 1 D array then can concated
# print(np.ndarray(array_2)) . can not possible