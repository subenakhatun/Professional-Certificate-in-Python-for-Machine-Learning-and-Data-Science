#  NumPy - Power and Square Root
import numpy as np
array_1 = np.array([10,20,30,40,50,60,70,80,90,50,60])
power = array_1**2
print(f'Power value manually: {power}')

# np.power(Array)
power1 = np.power(array_1,3)
print(f'Power value using numpy power method: {power1}')

# np.sqrt(array)
square = np.sqrt(array_1)
print(f'Square root using numpy method: {square}')