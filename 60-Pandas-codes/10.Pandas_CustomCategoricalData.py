# Example 10: Pandas - Creating Custom Categorical Data
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85, 70, 95, 60]}
df = pd.DataFrame(data)

# Creating a new column with categorical data
df['Performance'] = pd.cut(df['Score'], bins=[0, 70, 90, 100], labels=['A', 'V', 'C'])

print('DataFrame with Categorical Performance:\n', df)