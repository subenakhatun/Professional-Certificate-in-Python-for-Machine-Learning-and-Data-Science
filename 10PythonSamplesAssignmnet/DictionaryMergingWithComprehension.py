# Example 4: Dictionary Merging with Comprehension
# Merging two dictionaries and modifying values using dictionary comprehension.
# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

# Merging and modifying values
dict3 = set(dict1) | set(dict2)
print(dict3)
# merged_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}

# print('Merged and Modified Dictionary:', merged_dict)