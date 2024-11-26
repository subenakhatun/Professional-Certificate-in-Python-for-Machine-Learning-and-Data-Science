# Example 4: Pandas - Merging DataFrames with Different Keys
import pandas as pd

# df.merge(): 
'''
Merge types
merge() implements common SQL style joining operations.

one-to-one: joining two DataFrame objects on their indexes which must contain unique values.

many-to-one: joining a unique index to one or more columns in a different DataFrame.

many-to-many : joining columns on columns.
'''
# Creating two DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'Emp_ID': [2, 3, 4], 'Department': ['HR', 'Finance', 'IT']})
marge_data = pd.merge(df1,df2)
print(marge_data)