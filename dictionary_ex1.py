marks = {
    "Kannada": 85,
    "English": 90,
    "Maths": 78,
    "Science": 92,
    "Social": 88
}

# 1. Total marks
total = sum(marks.values())
print(f"Total marks: {total}")

# 2. Average marks
average = total / len(marks)
print(f"Average marks: {average}")

# 3. Highest mark subject
highest_subject = max(marks, key=marks.get)
print(f"Highest mark: {highest_subject} - {marks[highest_subject]}")
