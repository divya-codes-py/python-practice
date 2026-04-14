students = {
    "Divya": 95,
    "Rahul": 72,
    "Priya": 88,
    "Kiran": 65,
    "Suma": 91
}

# 1. Print students with score above 80
print("Students with score above 80:")
for name, score in students.items():
    if score > 80:
        print(f"  {name}: {score}")

# 2. Find highest score student
highest_student = max(students, key=students.get)
print(f"\nHighest score: {highest_student} - {students[highest_student]}")
