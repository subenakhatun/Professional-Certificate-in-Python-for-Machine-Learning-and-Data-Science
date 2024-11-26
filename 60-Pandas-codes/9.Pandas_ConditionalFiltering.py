# Example 9: Pandas - Conditional Filtering with Multiple Conditions
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
print(df,'\n') 
# want to show > 45 age values data

print(df[df['Age']>45])
