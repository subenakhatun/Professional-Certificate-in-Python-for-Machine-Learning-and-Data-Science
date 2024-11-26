# Example 12: Pandas - Shift and Lagging Data
import pandas as pd

# Creating a DataFrame
data = {'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
        'Temperature': [30, 32, 35, 33, 31]}
df = pd.DataFrame(data)

# Shifting data by one day to create a lag
# create new colum previsous day then i can use shift(position no start from here as like)
df['Prev Day Temp'] = df['Temperature'].shift(2)

print('DataFrame with Shifted Data:\n', df)

df['Privious Prevoius day Temperature'] = df['Temperature'].shift(2)
print('\n',df)