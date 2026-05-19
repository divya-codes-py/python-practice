# Sum of even and odd digits separately

num = int(input("Enter a number: "))

even_sum = 0
odd_sum = 0

while True:
    digit = num % 10

    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit

    num = num // 10

    if num == 0:
        break

print("Sum of even digits:", even_sum)
print("Sum of odd digits:", odd_sum)
