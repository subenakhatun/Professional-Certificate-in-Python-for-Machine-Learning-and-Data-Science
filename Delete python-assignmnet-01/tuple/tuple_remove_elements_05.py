# Example 5: Removing Elements from a Tuple
# Tuples are immutable, so elements cannot be removed directly.
# To remove elements, you need to convert the tuple to a list and back to a tuple.

my_tuple = (24,56,'ML',[4,5,6],{'Subjects:':['Mathematics','Statistics']},100,300,400,34,56)
my_list = list(my_tuple)
my_list.remove(24)
my_tuple = tuple(my_list)
print(my_tuple)

# Example tuple
my_tuple = (1, 2, 3, 4)

# Converting to a list and removing an element
temp_list = list(my_tuple)
temp_list.remove(2)
my_tuple = tuple(temp_list)

# Printing the tuple after removal
print('Tuple after Removal:', my_tuple)