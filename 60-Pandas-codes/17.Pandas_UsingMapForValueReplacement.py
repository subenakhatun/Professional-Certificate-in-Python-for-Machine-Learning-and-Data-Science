# Example 17: Pandas - Using map() for Value Replacement
import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Department': ['HR', 'IT', 'Finance'],
    'Subjects Code': [100,140,150]}
   
df = pd.DataFrame(data)

'''
Pandas is a widely used library for manipulating datasets. 
There are various in-built functions of pandas, one such function is pandas.map(), 
which is used to map values from two series having one similar column. For mapping two series, 
the last column of the first should be the same as the index column of the second series, also the 
values should be unique.
'''
# Mapping departments to codes
department_map = {'HR': 1, 'IT': 2, 'Finance': 3}
df['Dept Code'] = df['Department'].map(department_map)

print('DataFrame with Mapped Values:\n', df)

