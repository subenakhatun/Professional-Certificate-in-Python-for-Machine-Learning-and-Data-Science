
# Creating 2 arrays
import numpy as np
array_1 = np.array([10,20,30,40,50,60,70,80,90])
array_2 = np.array([9,8,7,6,5,4,3,2,1])

# Arithmetics operations: +,-,*,/. add,subtract,mutiply,divided

# np.add(arr1,arr2,...)
added = np.add(array_1,array_2)
print(f'Added arrays: {added}')

# np.subtract(arr1,arr2)
subtract = np.subtract(array_1,array_2)
print(f'Subtract arrays: {subtract}')

# np.multiply(arr1,arr2)
multiply = np.multiply(array_1,array_2)
print(f'Multiply arrays: {multiply}')

# np.divided(arr1,arr2)
divided = np.divide(array_1,array_2)
print(f'Divided arrays: {divided}')