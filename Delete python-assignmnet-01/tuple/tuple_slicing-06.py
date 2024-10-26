# Example 6: Tuple Slicing
# Slicing allows you to extract a part of the tuple.
# It is done using a colon (:) to specify start, stop, and step indices.

my_tuple = (24,56,'ML',[4,5,6],{'Subjects:':['Mathematics','Statistics']},100,300,400,34,56)

# Negative slicing
print('find last 4 no value to befor -1 no values: ',my_tuple[-4:-1])

# show 5 no postion to last values

print('show 5 no postion to last values: ',my_tuple[5:])

# beginning to 5 no postion
print('beginning to 5 no postion',my_tuple[:5])

# show evey odd position values
print('Every odd position values:',my_tuple[1::2])