# NumPy - Linear Space Array
import numpy as np

# Generating a linear space array with evenly spaced values. You can not make 2D array using linsapce
linear_space = np.linspace(0, 10, 5)# just create 5 values between 0 to and every vlaue gap must be same

print('Linear Space Array:', linear_space)

array_1 = np.linspace(10,100,10) # start form 10 and end 100 and make 10 number. must be deciam values. 
print(array_1)
# if you want to check type 
print(array_1.dtype)
