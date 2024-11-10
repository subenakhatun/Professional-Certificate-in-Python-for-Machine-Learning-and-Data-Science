# NumPy - Extracting Diagonal Elements
import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'Main Matrix: \n {matrix}')
print(f'every 1 columns rows values: \n {matrix[0:,-1:]}')
print(f'just show me 6 values: \n {matrix[1,2]}')
# Extracting the main diagonal
diagonal_elements = np.diag(matrix)

print('Diagonal Elements:', diagonal_elements)
