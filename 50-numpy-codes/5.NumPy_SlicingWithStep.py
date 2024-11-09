# Slicing with steps, start:end:step for 1D array
import numpy as np
array_1 = np.array([10,20,30,40,50,60,70,80,90,50,60])

# show 1st to last values every 2 steps
print(f'Show 1st to last all values but all odd no values: {array_1[::2]}')