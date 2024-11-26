# Example 7: Pandas - Melting DataFrames
import pandas as pd

# create a dataframe
data = {
    'Name': ['Subena','Subena1','Subena2','Subena3','Subena4','Subena5','Subena6'],
    'ID': [20241373,20241363,20241376,20241356,20241358,20241359,20241345],
    'Course':['STAT1','Sampling','DSA','ML','BIG Data','Elemnetary STAT','NONE'],
    'Age':[29,40,45,25,28,26,50],
    'Mobile No':[1894858170,78795,236958,789456,123654,789654,123654]
}
df = pd.DataFrame(data)
print(df)

# pd.melt()

'''
pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)
[source]
Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.

This function is useful to massage a DataFrame into a format where one or more columns are identifier variables (id_vars), while all other columns, considered measured variables (value_vars), are “unpivoted” to the row axis, 
leaving just two non-identifier columns, ‘variable’ and ‘value’.
'''
melted_df = pd.melt(df,id_vars='ID', value_vars=["Name",'Age'])
print(melted_df)