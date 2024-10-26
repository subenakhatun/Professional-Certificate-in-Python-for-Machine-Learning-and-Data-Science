# Example 2: Accessing Dictionary Values
# Values in a dictionary are accessed using their keys.
# If a key is not found, a KeyError will be raised unless you use the get() method, which returns None.
my_dic = {
    'name':['Subena','Shuly','Rahena','Farzana','Dhoha'],
    'Subjects':['Future Data Scientist','Home maker','Dreamer','Hridoyban','just beginning her life'],
    'Marks':[70,80,90,100,100],
    'Age':[30,35,31,32,18],
    'City':['Dhaka','Sylhet','Sylhet','Sylhet','Dhaka']       
}

# using keys
print(my_dic['name'][2])

# using index number not possible
# print(my_dic[2][1])
# using get methods: get(keyname)
dicvalue = my_dic.get('Age')
print(dicvalue)

# get keys using keys methods/ keys()
keyvalues = my_dic.keys()
print(keyvalues)

# just shows all vleus
allvalues = my_dic.values()
print('All values: ', allvalues)

# find value and keys at a time using items()

items = my_dic.items()
print(items)
for i in items:
    print(i)