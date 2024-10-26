# Example 7: Checking Membership in a Dictionary
# You can use the 'in' keyword to check if a key exists in a dictionary.

my_dic = {
    'name':['Subena','Shuly','Rahena','Farzana','Dhoha'],
    'Subjects':['Future Data Scientist','Home maker','Dreamer','Hridoyban','just beginning her life'],
    'Marks':[70,80,90,100,100],
    'Age':[30,35,31,32,18],
    'City':['Dhaka','Sylhet','Sylhet','Sylhet','Dhaka']       
}

# checking name is here or not
if 'name' in my_dic:
    print('yes')
else:
    print('No')