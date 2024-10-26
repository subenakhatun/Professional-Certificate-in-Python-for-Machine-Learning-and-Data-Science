# Example 7: Tuple Comprehension (using generator expression)
# Tuples do not support comprehension like lists.
# However, you can use a generator expression to create a tuple.

my_tuple = [10,20,30,40,50,60]
squared_tuple = tuple(x**2 for x in my_tuple)

# Printing the tuple
print('Squared Tuple:', squared_tuple)