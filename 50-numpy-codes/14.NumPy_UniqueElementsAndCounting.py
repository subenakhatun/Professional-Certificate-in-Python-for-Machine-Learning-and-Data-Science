# NumPy - Unique Elements and Counting. np.unique(array)
import numpy as np

# Creating an array with duplicate values
array = np.array([1, 2, 2, 3, 4, 4, 4, 5])

# Finding unique elements and their counts: if i don't write return counts then progmra error occured cz we declare 2 values ad a time
unique_elements, counts = np.unique(array, return_counts=True)

print('Unique Elements:', unique_elements)
print('Counts of Unique Elements:', counts)

# for 3d find unique values as a 1D array
array_3d = np.array([[[1, 1], [3, 19]], [[5, 5], [7, 8]], [[9, 10], [11, 11]]])
print(f'find unique values form 3D array {np.unique(array_3d)}')
print(f'find unique counts values form 3D array {np.unique_counts(array_3d)}')