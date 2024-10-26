# Example 7: List Comprehension
# List comprehension is a concise way to create lists using an expression and iteration.
# It can be used to generate new lists from existing ones.

# use list length
my_list = [34,40,55,80,96,35,70,29,85,49,70]
updated_list = []
for i in range(1,len(my_list)):
    updated_list.append(i**2)
print(updated_list)

# using list comprehension
updated_list = [i**3 for i in range(1,len(my_list))]
print(updated_list)

# use list values
my_list = [34,40,55,80,96,35,70,29,85,49,70]
updated_list = []
for i in my_list:
    updated_list.append(i**2)
print(updated_list)

# using list comprehension
updated_list = [i**3 for i in my_list]
print(updated_list)
