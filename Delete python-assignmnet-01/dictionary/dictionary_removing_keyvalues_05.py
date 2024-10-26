# Example 5: Removing Key-Value Pairs from a Dictionary
# You can remove key-value pairs using the pop() method, which removes the specified key and returns its value.
# The del keyword can also be used to remove a specific key or clear() to remove all items.

my_dic = {
    'name':['Subena','Shuly','Rahena','Farzana','Dhoha'],
    'Subjects':['Future Data Scientist','Home maker','Dreamer','Hridoyban','just beginning her life'],
    'Marks':[70,80,90,100,100],
    'Age':[30,35,31,32,18],
    'City':['Dhaka','Sylhet','Sylhet','Sylhet','Dhaka']       
}

# remove any key values using pop()

city = my_dic.pop('City')
print('After remove: ', my_dic)

# also use del(), clear() , popitem()