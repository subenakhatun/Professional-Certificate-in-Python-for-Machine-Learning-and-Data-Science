# Example 3: Tuple Immutability
# Tuples are immutable, meaning their values cannot be changed once created.
# Trying to modify an element of a tuple will result in an error.

my_tuple = (24,56,'ML',[4,5,6],{'Subjects:':['Mathematics','Statistics']},100,300,400,34,56)
try:
    my_tuple[0] = 24
except TypeError as e:
    print('Error:', e)