# Boolean indexing. true or false: condition use
import numpy as np

# create an simple array
array_1 = np.array([10,20,30,40,50,60,70,80,90,50,60])

# find less than 30 values

arr1 = array_1[array_1 < 30]
print(arr1)