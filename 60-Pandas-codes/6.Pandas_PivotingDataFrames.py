# Example 6: Pandas - Pivoting DataFrames
import pandas as pd

# Creating a DataFrame
data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'],
        'City': ['NY', 'NY', 'LA', 'LA'],
        'Sales': [200, 250, 300, 400]}
df = pd.DataFrame(data)

# Pivoting the DataFrame
# try to improve you common sense in this pivot and also pivot table subena. 
pivot_df = df.pivot(index='Date', columns='City', values='Sales')
pivot_df1 = df.pivot(index='City', columns='Sales', values = 'Date')

print('Pivoted DataFrame:\n', pivot_df)
print('\n',pivot_df1)