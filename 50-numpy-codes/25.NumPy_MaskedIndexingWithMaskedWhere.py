# NumPy - Masked Indexing with np.ma.masked_where
import numpy as np

# Creating an array
array = np.array([1, -2, 3, -4, 5,10,9,56,80,70,3,78])

# Masking elements where values are negative
masked_array = np.ma.masked_where(array < 0, array)

print('Masked Array with Negative Values Hidden:', masked_array)