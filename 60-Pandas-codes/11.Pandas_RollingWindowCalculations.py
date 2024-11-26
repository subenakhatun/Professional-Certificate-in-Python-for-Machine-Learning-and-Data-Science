# Example 11: Pandas - Rolling Window Calculations
import pandas as pd

# Creating a time series DataFrame
date_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = {'Sales': [100, 200, 150, 300, 250, 400, 300, 350, 300, 400]}
df = pd.DataFrame(data, index=date_range)

# Calculating a rolling mean with a window of 3 days
# window 3 means por por 3 ta value niye kaj kora
# important ase . data analysis a kaj a lagbe
df['Rolling Mean'] = df['Sales'].rolling(window=3).mean()

df['New columns Sum'] = df['Sales'].rolling(window=4).sum()
print('DataFrame with Rolling Mean:\n', df)

average = (150+300+250)/3
print(average)