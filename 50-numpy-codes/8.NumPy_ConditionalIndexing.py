# NumPy - Conditional Indexing
import numpy as np
# Creating an array
array = np.array([1, 2, 3, 4, 5, 6])

# Setting elements that satisfy a condition
array[array % 2 == 0] = -1  # Set even numbers to -1

print('Array after Conditional Indexing:', array)

array[array % 3 == 1] = 19
print(array)
