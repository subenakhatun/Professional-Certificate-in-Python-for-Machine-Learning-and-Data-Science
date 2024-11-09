# Creating an array

import numpy as np
array_1 = np.array([1,2,3,4,5,5,6,7,8])
print(array_1)

# accessing elements by index: index start from 0
print(f'Print 2 no position value: {array_1[3]}')

# negative indexing
# print last values
print(f'Print last value: {array_1[-1]}')

# slicing
# print 2no to 5 no position values
print(f'Show from 2nd to 5th no values: {array_1[1:5]}')

# print every odd position values: start, end, step
print(f'All odd postion values: {array_1[0:7:2]}')