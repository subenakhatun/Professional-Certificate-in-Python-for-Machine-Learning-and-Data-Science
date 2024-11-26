# Example 15: Pandas - Handling Outliers
import pandas as pd
import numpy as np

# Creating a DataFrame
data = {'Value': [10, 12, 14, 100, 15, 13, 12,120,800,720,650,1,89,56,74,135,168]}
df = pd.DataFrame(data)

# Identifying outliers using the IQR method
Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)
# inter quartile range(IQR). 25% = Q1, 75% = Q3, 50% = Q2 or medium
IQR = Q3 - Q1
# Outliers: (Q1 - 1.5 * IQR) and (Q3 + 1.5 * IQR)
outliers = df[(df['Value'] < (Q1 - 1.5 * IQR)) | (df['Value'] > (Q3 + 1.5 * IQR))]

print('Outliers:', outliers)
print(df['Value'].count())
