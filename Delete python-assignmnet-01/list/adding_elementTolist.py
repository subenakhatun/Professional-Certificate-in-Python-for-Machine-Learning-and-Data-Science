# Example: 04
'''
1. list.append(elem) -- adds a single element to the end of the list.
2. list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
3. list.extend(list2) adds the elements in list2 to the end of the list.
'''

my_list = [300, 40, 55, 96, 35, 70, 49, 10]
# list.append(elem)
my_list.append(4)
print(my_list)

# list.insert(index, elem)
my_list.insert(4,'Inserted')
print(my_list)

# another list
my_list1 = ['NLP',"CV"]

# list.extend(list2)
my_list.extend(my_list1)
print(my_list)