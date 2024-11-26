# Example 20: Pandas - Using Rank to Rank Values
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85, 90, 78, 92]}
df = pd.DataFrame(data)

# Ranking scores in descending order
df['Rank'] = df['Score'].rank(ascending=False)

print('DataFrame with Ranked Scores:\n', df)
# create a dataframe
data = {
   'Name': ['Subena','Subena1','Subena2','Subena3','Subena4','Subena5','Subena6'],
    'ID': [20241373,20241363,20241376,20241356,20241358,20241359,20241345],
    'Course':['STAT1','Sampling','DSA','ML','BIG Data','Elemnetary STAT','NONE'],
    'Age':[29,40,45,25,28,26,50],
    'Mobile No':[1894858170,78795,236958,789456,123654,789654,123654]
}
df1 = pd.DataFrame(data)
df1['Rank of students'] = df1['Age'].rank()
print(df1)