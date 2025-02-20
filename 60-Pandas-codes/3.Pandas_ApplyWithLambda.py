# Example 3: Pandas - Using Apply with Lambda Functions create another new columns for this dataset
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Subena', 'Rahena', 'Shuly'], 'Score': [85, 90, 95]}
df = pd.DataFrame(data)
print(df)

# Applying a lambda function to modify scores
df['Adjusted Score'] = df['Score'].apply(lambda x: x + 5 if x < 90 else x)
print(df['Adjusted Score'] )
print(df)  
# undersatnd 
def Adjusted_score(x):
    if x < 90:
        print(x+5)
    else:
        print(x)
df['Score'].apply(Adjusted_score)

# print('DataFrame with Adjusted Scores:\n', df)
