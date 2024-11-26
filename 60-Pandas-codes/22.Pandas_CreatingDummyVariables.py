
# Example 22: Pandas - Creating Dummy Variables
import pandas as pd

# Creating a DataFrame
data = {'City': ['NY', 'LA', 'SF', 'NY']}
df = pd.DataFrame(data)

# Creating dummy variables
dummies = pd.get_dummies(df['City'], prefix='City')

# no nedd to make any dummy data. already huge data so i don't want to make me confused more enough
print('Dummy Variables DataFrame:\n', dummies)
