# Reverse a number

num = int(input("Enter a number: "))

reverse = 0

while True:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

    if num == 0:
        break

print("Reversed number is:", reverse)
