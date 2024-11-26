# Example 18: Pandas - Detecting Duplicates
import pandas as pd

# Creating a DataFrame with duplicate rows
data = {
    'ID': [1, 2, 2, 3, 4, 4], 
    'Value': [10, 20, 20, 30, 40, 40]}
df = pd.DataFrame(data)

# Detecting duplicates
duplicates = df[df.duplicated()]

print('Duplicate Rows:\n', duplicates)

# Creating a DataFrame
data = {
    'City': ['NY', 'LA', 'NY', 'SF', 'LA','NY', 'LA', 'NY', 'SF', 'LA','NY', 'LA', 'NY'], 
    'Year': [2020, 2020, 2021, 2021, 2020,2022,2023,2024,2026,2020,2023,2021,2025],
    'Sales': [100, 150, 200, 250, 300,120,560,230,820,450,260,230,520]}
df = pd.DataFrame(data)
dup = df.duplicated().count()
print(dup)