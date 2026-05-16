# Problem 9: Factorial of a given number

n = int(input("Enter a number: "))
result = 1
i = 1
while i <= n:
    result *= i
    i += 1
print(f"Factorial of {n} = {result}")
