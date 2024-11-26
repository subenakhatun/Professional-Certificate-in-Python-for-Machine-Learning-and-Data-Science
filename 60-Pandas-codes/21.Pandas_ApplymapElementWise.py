# Example 21: Pandas - Using applymap for Element-wise Operations
import pandas as pd

# Creating a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Applying an operation to each element in the DataFrame
# no need to apply it. i can use it which colum i want to apply this lamba function
df_transformed = df.applymap(lambda x: x**2)
df_new = df['B'].apply(lambda x: x**3)

print('DataFrame with Squared Values:\n', df_transformed)
print(df_new)