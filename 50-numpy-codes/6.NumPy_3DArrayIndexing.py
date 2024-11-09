#  NumPy - 3D Array Indexing
import numpy as np
# Create a 3D array
array_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
# print(array_3d)

# accessing 3D array
element = array_3d[1, 0, 1]  # 1st row, 0 row, then 1 colum value
print(element)

# find 0 no row , 0 no row and 0 colum values: 1
print(array_3d[0, 0, 0])

# find the value 10
print(array_3d[1, 1, 0])

# Slicing in 3D 
print(array_3d[:, 0, 2]) # : 1st to last, 0 every 1st row, 