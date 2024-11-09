# NumPy - Broadcasting
import numpy as np

# Creating an array
array = np.array([1, 2, 3])

# Broadcasting: Adding a scalar to an array for every value
result = array + 10

print('Original Array:', array)
print('Array after Broadcasting:', result)
print(f'Subtract {array-10}')
print(f'Multiply {array*6}')