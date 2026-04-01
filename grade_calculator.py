marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"
    message = "Outstanding! 🌟"
elif marks >= 80:
    grade = "A"
    message = "Well done! 🎉"
elif marks >= 70:
    grade = "B"
    message = "Good job! 😊"
elif marks >= 60:
    grade = "C"
    message = "Keep trying! 💪"
elif marks >= 50:
    grade = "D"
    message = "Need improvement! 📖"
else:
    grade = "F"
    message = "Please study more! 📚"

print(f"Your Grade: {grade}")
print(message)
