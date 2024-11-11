# NumPy - Extracting Upper Triangle of a Matrix. np.triu(array)
import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'Orginal array or matrix: {matrix}')
print(f'Upper traiangular Matrix: {np.triu(matrix)}')
# 3D array 
array_3 = np.array([[[1,2,3,4],[4,5,6,7]],[[7,8,9,0],[10,3,5,6]],[[76,8,90,0],[10,33,5,62]]])
print(f'3D orginal martix: \n {array_3}')
print(f'Upper traiangular 3D Matrix: \n {np.triu(array_3)}')