

my_dic = {
    'name':['Subena','Shuly','Rahena','Farzana','Dhoha'],
    'Subjects':['Future Data Scientist','Home maker','Dreamer','Hridoyban','just beginning her life'],
    'Marks':[70,80,90,100,100],
    'Age':[30,35,31,32,18],
    'City':['Dhaka','Sylhet','Sylhet','Sylhet','Dhaka']       
}

# change values
my_dic['name'][2] = 'Unknown'
print('updated dict: ', my_dic['name'])

# update using update()
my_dic.update({'class': 'Do not know'})
print('updated dict: ', my_dic['class'])