# Example 19: Pandas - Using Explode for Lists in Columns
import pandas as pd

# Creating a DataFrame with lists in a column
data = {
    'ID': [1, 2], 
    'Hobbies': [['Reading', 'Swimming'], ['Running', 'Cycling']]}
df = pd.DataFrame(data)
# Transform each element of a list-like to a row, replicating index values.
# Exploding the 'Hobbies' column
exploded_df = df.explode('Hobbies')
print(df)
print('DataFrame after Exploding Lists:\n', exploded_df)

# Creating a DataFrame
data = {
    'City': ['NY', 'LA', 'NY', 'SF', 'LA','NY', 'LA', 'NY', 'SF', 'LA','NY', 'LA', 'NY'], 
    'Year': [2020, 2020, 2021, 2021, 2020,2022,2023,2024,2026,2020,2023,2021,2025],
    'Sales': [[100, 150], [200, 250], [300,120],[560,230],[820,450],[260,230],[520,520],[100, 150], [200, 250], [300,120],[560,230],[820,450],[260,230]]}
df1 = pd.DataFrame(data)

# print(df1)
another_explode = df1.explode('Sales')
print(another_explode)