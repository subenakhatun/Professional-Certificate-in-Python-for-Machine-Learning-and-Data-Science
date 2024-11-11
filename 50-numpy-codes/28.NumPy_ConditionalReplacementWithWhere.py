# NumPy - Conditional Replacement with np.where
import numpy as np

# Creating an array
array = np.array([10, 15, 20, 25, 30])

# Replacing values based on condition
result = np.where(array > 20, 0, array)

print('Array with Values Greater Than 20 Replaced with 0:', result)
