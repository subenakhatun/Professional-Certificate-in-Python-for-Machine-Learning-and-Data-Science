
# Example 13: Pandas - Cumulative Sum and Product
import pandas as pd

# Creating a DataFrame
data = {'Sales': [100, 200, 150, 300, 250]}
df = pd.DataFrame(data)

# create a dataframe
data = {
   'Name': ['Subena','Subena1','Subena2','Subena3','Subena4','Subena5','Subena6'],
    'ID': [20241373,20241363,20241376,20241356,20241358,20241359,20241345],
    'Course':['STAT1','Sampling','DSA','ML','BIG Data','Elemnetary STAT','NONE'],
    'Age':[29,40,45,25,28,26,50],
    'Mobile No':[1894858170,78795,236958,789456,123654,789654,123654]
}
df = pd.DataFrame(data)

# Calculating cumulative sum and product and add columns into dataset
df['Comulative Sum of Age'] = df['Age'].cumsum()
df['Comulative Product of age'] = df['Age'].cumprod()
print(df)
