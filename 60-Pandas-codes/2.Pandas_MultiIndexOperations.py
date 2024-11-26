# Example 2: Pandas - MultiIndex DataFrame Operations

import pandas as pd
arrays = [['A', 'A', 'B', 'B'], [2020, 2021, 2020, 2021]]
index = pd.MultiIndex.from_arrays(arrays, names=['Category','year'])
print(arrays)
print(index)
data = [10,50,40,60]
df = pd.DataFrame(data, columns=['Values'], index=index)
print(df)
# don't think so is this necessary or not. confused where and wehn it use
sale = df.xs(2020, level='year')
print(sale)