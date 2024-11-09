#  NumPy - Transposing Arrays: rows into columns and columns into rows
import numpy as np
# Create a 2d array then tranpose it
arrat_1 = np.array([[10,20,30],[40,50,60]])
print(f'Main 2D array {arrat_1}')
print(f'Transpose 2D array {np.transpose(arrat_1)}')

# Create a 1d array then tranpose it: not working for 1D . so sad
array_2 = np.array([10,80,90,40,50,60,20,30,10])
print(f'Main 1d array {array_2}')
print(f'After transposing 1D array {np.transpose(array_2)}')