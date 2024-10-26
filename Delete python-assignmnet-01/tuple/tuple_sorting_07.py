# Example 7: Sorting a Tuple
# Tuples are immutable and cannot be sorted directly.
# To sort a tuple, you need to convert it to a list, sort it, and convert it back to a tuple.
my_tuple = [10,20,30,40,50,60,3,78,90,13]
squared_tuple = tuple(x**2 for x in my_tuple)

# Printing the tuple
print('Squared Tuple:', squared_tuple)

number_tuple = (5, 2, 9, 1, 5, 6)

# Sorting by converting to a list
sorted_list = sorted(my_tuple)
sorted_tuple = tuple(sorted_list)

# Printing the sorted tuple
print('Sorted Tuple:', sorted_tuple)
