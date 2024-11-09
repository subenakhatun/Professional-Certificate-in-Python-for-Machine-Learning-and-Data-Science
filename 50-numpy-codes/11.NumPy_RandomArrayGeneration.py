# NumPy - Random Array Generation
import numpy as np

# Generating random arrays
random_array = np.random.rand(3, 3)  # Random values in a 3x3 array
normal_array = np.random.randn(3, 3)  # Random values with a normal distribution. integer values

print(f'Random Array:\n {random_array}')
print(f'Normal Distribution Array:\n {normal_array}')

# from 3 to 5 integer value 
random_array_2 = np.random.randint(3,5)
print(f'from 3 to 5 integer value {random_array_2}')
# from 3 to 8 integer value 
random_array_2 = np.random.randint(3,8) # any one value just print
print(f'from 3 to 8 integer value {random_array_2}')