# Find sum of digits

num = int(input("Enter a number: "))

sum = 0

while True:
    digit = num % 10
    sum += digit
    num = num // 10

    if num == 0:
        break

print("Sum of digits:", sum)
