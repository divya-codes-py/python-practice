int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
operation = input("Enter your operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("You entered a wrong operation!")

print(f"\n---- Calculator Result ----")
print(f"{num1} {operation} {num2} = {result}")
