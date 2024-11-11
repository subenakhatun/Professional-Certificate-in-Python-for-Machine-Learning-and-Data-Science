# NumPy - Clipping Array Values
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5])

# Clipping values to be between 2 and 5
clipped_array = np.clip(array, 2,5)

print(f'Original Array:{array}')
print(f'Clipped Array:{clipped_array}')
