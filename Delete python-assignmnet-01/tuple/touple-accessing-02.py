# Example 2: Accessing Tuple Elements
# Elements in a tuple are accessed using indices, similar to lists.
# Indexing starts from 0 (first element) and can also be negative (-1 for the last element).

my_tuple = (24,56,'ML',[4,5,6],{'Subjects:':['Mathematics','Statistics']})
# see lenth of the tuple
print(len(my_tuple))

# access 2 no postion using index number
print('2nd position value:', my_tuple[2])

# Negative indexing: find last value of the tuple
print('Last valuee: ',my_tuple[-1])