
# Example 9: Dictionary Filtering Based on Conditions
# Filtering a dictionary to retain only key-value pairs that satisfy a condition.

students_marks = {
'Name':['Barlowe','Caddel','Madden'],
'Subjects': ['English','Computer Science','Physics'],
'Marks': [80,94,86],
'Passing Year':[2021,2022,2023]                         
}
print(students_marks)
# Filtering to retain scores >= 80

for name, value in students_marks:
    print(value)