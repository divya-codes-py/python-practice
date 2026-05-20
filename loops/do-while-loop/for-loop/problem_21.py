# Sum of odd numbers from 1 to n

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1, 2):
    total += i

print("Sum of odd numbers:", total)
