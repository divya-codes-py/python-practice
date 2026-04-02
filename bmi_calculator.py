weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height * height)
bmi = round(bmi, 2)

print(f"BMI: {bmi}")

if bmi < 18.5:
    print("Category: Underweight 😟")
elif bmi < 25:
    print("Normal weight ✅ ")
elif bmi < 30:
    print(" Overweight ⚠️")
else:
    print("Obese 🔴")
