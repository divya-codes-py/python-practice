students = ["Divya", "Rahul", "Priya", "Kiran"]
marks = [95, 72, 88, 65]

# All students dictionary
all_students = {students[i]: marks[i] for i in range(len(students))}
print(f"All students: {all_students}")

# 80 kante jaasti filter
toppers = {name: mark for name, mark in all_students.items() if mark > 80}
print(f"Toppers: {toppers}")
