
# Example 9: Dictionary Filtering Based on Conditions
# Filtering a dictionary to retain only key-value pairs that satisfy a condition.

students_marks = {
'Name':['Barlowe','Caddel','Madden'],
'Subjects': ['English','Computer Science','Physics'],
'Marks': [80,94,86],
'Passing Year':[2021,2022,2023]                         
}
# print(students_marks)
# show 80 marks
empty = []
for name, value in students_marks.items():
    for value_position in value:
        if value_position == 80:
            print(f'{name}: {value_position}')
    # print(name,value[0])

# find keys, values pair
for name, value in students_marks.items():
    print(name,value)