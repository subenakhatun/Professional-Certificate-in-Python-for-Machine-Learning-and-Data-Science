# Example 5: Set Intersection
# The intersection() method returns a new set containing common elements from both sets.
# You can also use the & operator to perform the intersection operation.

my_set = {'subena',30,10,20,30,78,50,62,89}
my_set1 = {700,800,900,10,20,30,89}
new_set = my_set.intersection(my_set1)
print(new_set) 

my_set2 = {'subena','khatun',10,600}
new_set1 = my_set & my_set2
print(new_set1)