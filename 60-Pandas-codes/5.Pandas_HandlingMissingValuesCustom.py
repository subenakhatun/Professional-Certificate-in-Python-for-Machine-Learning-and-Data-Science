# Example 5: Pandas - Handling Missing Values with Custom Functions
import pandas as pd
import numpy as np
# Creating a DataFrame with missing values
data = {'Name': ['Alice', 'Bob', np.nan, 'David'], 'Age': [25, np.nan, 35, 40]}
df = pd.DataFrame(data)

# Filling missing values using a custom function
print(df)
print('\n')
# check mising value
# print(df.isnull)
df['Name'] = df['Name'].fillna('Subena')
df['Age'] = df['Age'].fillna(30)
print(df)
