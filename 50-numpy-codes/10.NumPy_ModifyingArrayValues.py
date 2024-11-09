# NumPy - Modifying Array Values using Indexing
import numpy as np

# Creating an array
array_1 = np.array([10, 20, 30, 40, 50])

# Modifying values at specific indices: positon number 1 and 3 values will be replace by 100 and 200
array_1[[1, 3]] = [100, 200]

print('Modified Array:', array_1)