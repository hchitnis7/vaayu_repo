
students = {"name": ["Harsh", "meow"], "M_name": ["pallavi", "tata"], "L_name" : ["Chitnis", "bajaj"]}
print(students)
print(students.items())
print(students.keys())
students_1 = students.copy()
students_1.pop("M_name")
print(students_1)
students_1.update(students)
print(students_1)
print(students_1.get("name"))