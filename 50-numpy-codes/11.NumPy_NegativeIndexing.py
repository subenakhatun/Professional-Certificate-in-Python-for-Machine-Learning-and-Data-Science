# NumPy - Indexing with Negative Indices
import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50,60,70,80,90,100])

# Accessing elements from the end using negative indices
last_element = array[-1]
second_last_element = array[-2]
thirdToLast = array[3:]
lastToFirst = array[-1:0:-1]

print(f'Last Element:{last_element}')
print(f'Second Last Element:{second_last_element}')
print(f'Third Last Element:{thirdToLast}')
print(f'Last to  First Element:{lastToFirst}')