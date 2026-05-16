# Problem 8: Sum of all odd numbers from 1 up to n

n = int(input("Enter a number: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 2
print(f"Sum of odd numbers up to {n} = {total}")
