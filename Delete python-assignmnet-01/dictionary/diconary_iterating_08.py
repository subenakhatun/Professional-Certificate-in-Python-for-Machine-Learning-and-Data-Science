# Example 8: Iterating Over a Dictionary
# You can iterate over a dictionary to access its keys, values, or key-value pairs.


my_dic = {
    'name':['Subena','Shuly','Rahena','Farzana','Dhoha'],
    'Subjects':['Future Data Scientist','Home maker','Dreamer','Hridoyban','just beginning her life'],
    'Marks':[70,80,90,100,100],
    'Age':[30,35,31,32,18],
    'City':['Dhaka','Sylhet','Sylhet','Sylhet','Dhaka']       
}

for key, value in my_dic.items():
    print(f'Key: {key}, Value: {value}')