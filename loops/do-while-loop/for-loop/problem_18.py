# Print numbers divisible by 7

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(a, b + 1):
    if i % 7 == 0:
        print(i)
