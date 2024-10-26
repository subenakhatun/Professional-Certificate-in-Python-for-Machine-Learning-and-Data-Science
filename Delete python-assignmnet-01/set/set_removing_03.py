# Example 3: Removing Elements from a Set
# You can remove elements using the remove() or discard() methods.
# The remove() method raises an error if the element is not found, while discard() does not.
# To remove an item in a set, use the remove(), or the discard() method
# create a set
my_set = {'subena',30,10,20,30,78,50,62,89}
my_set.remove('subena')
print(my_set)
my_set.discard(89)
print(my_set)