# 2D array Indexing
import numpy as np
# Creaitng 2D array
array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print and show is it 2d or none
print(array_2d)

# Accessing individuals elements. Indexing start form 0 not 1
# 2 no row and 2 no columns value
print(f' 2 no row and 2 no colunm values: {array_2d[1,1]}')

# Slicing rows and columns
# first row and all columns
print(f' 1st row and all colunms value: {array_2d[0, :]}')
# 3rd  row and all columns
print(f' 1st row and all colunms value: {array_2d[2, :]}')

# all rows but 3rd columns
print(f' every rows, 3rd column values: {array_2d[:, 2]}')