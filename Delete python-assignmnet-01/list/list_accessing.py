'''
What is accessing list in Python?
** Python list elements are ordered by index, a number referring to their placement in the list. 
** List indices start at 0 and increment by one. also can accessing form -1
** To access a list element by index, square bracket notation is used: list[index] .
'''
# create a integer list
my_list = [34,40,55,80,96,35,70,29,85,49,70]
first_element = my_list[1]
last_element = my_list[-1]
position_element = my_list[4]

# accessing first element
print('First Element:',first_element)
print('First Element:',my_list[1])

# accessing last elemnet. Negative indexing
print('Last Element:',last_element)
print('Last Element:',my_list[-1])

# accessing 5th no position element
print('5th position Element:',position_element)
print('5th position Element:',my_list[4])
