
# Example 14: Pandas - Merging on Multiple Columns
import pandas as pd

# Creating two DataFrames
# create a dataframe
data = {
   'Name': ['Subena','Subena1','Subena2','Subena3','Subena4','Subena5','Subena6'],
    'ID': [20241373,20241363,20241376,20241356,20241358,20241359,20241345],
    'Course':['STAT1','Sampling','DSA','ML','BIG Data','Elemnetary STAT','NONE'],
    'Age':[29,40,45,25,28,26,50],
    'Mobile No':[1894858170,78795,236958,789456,123654,789654,123654]
}
df = pd.DataFrame(data)
print(df,'\n')
df1 = pd.DataFrame({'ID': [1, 2, 3,4,5,6,7], 'Year': [2020, 2021, 2021,2023,2024,2025,2026], 
                    'Name': ['Alice', 'Bob', 'Charlie','Ami','Maisha','Mitul','Shafali']})
df2 = pd.DataFrame({'ID': [2, 3, 1], 'Year': [2021, 2021, 2020], 'Score': [88, 92, 75]})

# Merging on multiple columns
merged_df = pd.merge(df, df1, on=['ID', 'Name'], how='outer')

print('Merged DataFrame on Multiple Columns:\n', merged_df)
