# Example 4: Adding Elements to a Tuple
# Tuples are immutable, so you cannot add elements directly.
# However, you can create a new tuple by concatenating the existing one with another tuple.


my_tuple = (24,56,'ML',[4,5,6],{'Subjects:':['Mathematics','Statistics']},100,300,400,34,56)

# tuple can not update any valu by using index position
# my_tuple[2] = 'subena'
# print(my_tuple)

# concatenate any value with tuple then create new tuple
print(my_tuple + (4,))

# another way: at disrt convert into list as type conversion list then  update its value then convert it into again tuple
x = list(my_tuple)
x[0] = 'subena'
tuple_convert = tuple(x)
print('print new tuple',tuple_convert ) # kushi kushi

print(type(tuple_convert))