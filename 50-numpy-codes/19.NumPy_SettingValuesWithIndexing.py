# NumPy - Setting Values Using Indexing
import numpy as np

array_1 = np.array([78,90,56,84,82])
array_1[[3,1]] = [100,200]
print(f'Replace values: {array_1}')

array_2 = np.array([[10,20,40],[30,60,23],[40,10000,50]])
print(f'Orginal String array: \n {array_2}')
# 0 no row and 1 no row , 2 no columns
array_2[[0,1],[2,2]] = [400,500]
print(f'Updated String array: \n {array_2}')
# 0 no row and 1 no row , 2 no columns and 1 no columns
array_2[[0,1],[2,1]] = [800,533300]
print(f'Updated String array: \n {array_2}')
