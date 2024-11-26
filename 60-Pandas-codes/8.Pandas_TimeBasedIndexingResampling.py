# Example 8: Pandas - Time-based Indexing and Resampling
import pandas as pd

# Creating a time series DataFrame
date_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = {'Sales': [100, 200, 150, 300, 250, 400, 300, 350, 300, 400]}
df = pd.DataFrame(data, index=date_range)
print(df)
# Resampling to find weekly sales
# 1-7 dates sale summation
# impotant when use in data analysis
weekly_sales = df.resample('W').sum()

print('Weekly Sales:\n', weekly_sales)
# print(pd.date_range(start='2018-04-24', end='2018-04-27', periods=10))