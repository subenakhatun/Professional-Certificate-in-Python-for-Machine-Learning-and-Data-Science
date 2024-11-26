
# Example 16: Pandas - Creating a Pivot Table with Multiple Aggregations
import pandas as pd

'''
A pivot table is a tool that summarizes large amounts of data in an interactive way. 
It allows users to analyze data, identify relationships between data points, and answer 
questions about their data
'''

# Creating a DataFrame
data = {
    'City': ['NY', 'LA', 'NY', 'SF', 'LA','NY', 'LA', 'NY', 'SF', 'LA','NY', 'LA', 'NY'], 
    'Year': [2020, 2020, 2021, 2021, 2020,2022,2023,2024,2026,2020,2023,2021,2025],
    'Sales': [100, 150, 200, 250, 300,120,560,230,820,450,260,230,520]}
df = pd.DataFrame(data)

# Creating a pivot table with multiple aggregations
pivot_table = pd.pivot_table(df, values='Sales', index='City', columns='Year', aggfunc=['sum', 'mean'])

print('Pivot Table with Multiple Aggregations:\n', pivot_table)
