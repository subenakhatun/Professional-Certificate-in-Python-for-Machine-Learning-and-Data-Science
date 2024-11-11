# NumPy - Cumulative Sum and Product. np.cumsum(array), np.cumprod(array)
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4])
print(f'Original array. {array}')
print(f'Cumulative sum: {np.cumsum(array)}')
print(f'Cumulative Product: {np.cumprod(array)}')