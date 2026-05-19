# Factorial of every number from 1 to n

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    fact = 1

    for j in range(1, i + 1):
        fact *= j

    print("Factorial of", i, "is", fact)
