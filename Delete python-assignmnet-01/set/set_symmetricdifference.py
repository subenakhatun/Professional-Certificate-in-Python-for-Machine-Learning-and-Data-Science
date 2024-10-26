# Example 7: Set Symmetric Difference
# The symmetric_difference() method returns a new set containing elements present in either set but not in both.
# You can also use the ^ operator to perform the symmetric difference operation.
# Example sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Performing symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2)

# Printing the symmetric difference set
print('Symmetric Difference of Sets:', symmetric_difference_set)