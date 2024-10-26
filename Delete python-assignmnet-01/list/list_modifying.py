# Example: 03. List modifying
'''
** list is mutable so any value can be change using it's index position assign.
To modify a specific element in a list using indexes in Python, you can access the element by 
its index and assign a new value to it. 
Indexes in Python are zero-based, meaning the first element in a list has an index of 0, 
the second element has an index of 1
'''

my_list = [34,40,55,80,96,35,70,29,85,49,70]

# Modifying the last , first  and 4th element
my_list[-1] = 10
my_list[0] = 300
my_list[3] = 300

# modifying by dictonary
my_list[3] = {'Subejcts':['NLP','CV',"Artificial brain"]}
# Printing the modified list
print('Modified List:', my_list)
