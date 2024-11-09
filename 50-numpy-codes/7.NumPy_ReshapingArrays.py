# NumPy - Reshaping Arrays: array.reshape((tuple value or number)). Means create 1d into 2D or 2D into 3D or 2D into 1 D
import numpy as np
array_1 = np.array([1, 2, 3, 4, 5, 6])
reshape_array = array_1.reshape((3,2)) # 3 rows and 2 columns: total 6 values distribution
print(f'Cobvert 2D from 1D {reshape_array}')
