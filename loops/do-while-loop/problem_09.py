# Find factorial using do-while logic

num = int(input("Enter a number: "))

fact = 1
i = 1

while True:
    fact *= i
    i += 1

    if i > num:
        break

print("Factorial is:", fact)
