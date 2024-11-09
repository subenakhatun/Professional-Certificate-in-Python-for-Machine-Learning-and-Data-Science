# NumPy - Trigonometric Functions: sin/cos/tan(array)
import numpy as np

# Crete an angle array 
array_angles = np.array([0, np.pi/3, np.pi/2,np.pi, np.pi/6])
print(f'Sin Angles  values: {np.sin(array_angles)}')
print(f'Cos Anglesvalues: {np.cos(array_angles)}')
print(f'Tan Angles values: {np.tan(array_angles)}')