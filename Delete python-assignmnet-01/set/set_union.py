# Example 4: Set Union
# The union() method returns a new set containing all unique elements from both sets.
# You can also use the | operator to perform the union operation.

my_set = {'subena',30,10,20,30,78,50,62,89}
my_set1 = {700,800,900,10,20,30,89}
new_set = my_set.union(my_set1)
print(new_set) 

my_set2 = {'subena','khatun',10,600}
new_set1 = my_set | my_set2
print(new_set1)