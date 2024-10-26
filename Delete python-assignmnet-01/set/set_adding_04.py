# Example 2: Adding Elements to a Set
# You can add elements to a set using the add() method.
# Sets do not allow duplicate elements.

# Create a set
my_set = {'subena',30,10,20,30}
my_set.add(100)
print(my_set)
# using update() and combine 2 sets

my_set1 = {78,50,62,89}
my_set.update(my_set1)
print('Updated set: ',my_set)