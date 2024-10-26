# Example 6: List Slicing
'''
In #python, slicing is an operation of slicing a list. 
This means that it can extract some elements from a list using some preferred indexes. 
It allows you to select a range of elements from a list by creating a shallow copy of a list 
containing only those elements.
'''
# Slicing allows you to extract a part of the list.
# It is done using a colon (:) to specify start, stop, and step indices.

# my list
my_list = [34,40,55,80,96,35,70,29,85,49,70]

# slicing to 4th position to last
print(my_list[4:])

# first to 6 but every 2 step
print(my_list[0:6:2])

# last to first or reverse a list
print(my_list[-1:-11:-1])