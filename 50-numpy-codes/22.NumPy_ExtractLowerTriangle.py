# NumPy - Extract Lower Triangle of a Matrix
import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'Orginal array or matrix: \n {matrix}')
print(f'Lower traiangular Matrix: \n {np.tril(matrix)}')