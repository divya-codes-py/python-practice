# Sum of even numbers from 1 to n

n = int(input("Enter a number: "))

total = 0

for i in range(2, n + 1, 2):
    total += i

print("Sum of even numbers:", total)
