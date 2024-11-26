import pandas as pd

# Creating a DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'C', 'C', 'A'],
        'Value': [10, 20, 15, 25, 35, 45, 30]}
df = pd.DataFrame(data)
grouped = df.groupby('Category').agg(sum)
print(grouped)
# Grouping by 'Category' and calculating the sum and mean
grouped = df.groupby('Category').agg({'Value': ['sum', 'mean']})

# print('Grouped DataFrame with Aggregations:\n', grouped)
# confused
