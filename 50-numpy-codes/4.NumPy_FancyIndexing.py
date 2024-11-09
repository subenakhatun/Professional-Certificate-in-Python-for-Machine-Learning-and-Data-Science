# numpy Fancy indexing
import numpy as np
array_1 = np.array([10,20,30,40,50,60,70,80,90,50,60])
# using id 1D array
# slecting specing postion values
print(f'Show 3 no {array_1[3]} , 5 no {array_1[5]} and 7 no {array_1[7]} vlaues {array_1[[3,5,7]]}')