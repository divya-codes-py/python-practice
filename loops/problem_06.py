# Problem 6: Sum of first n natural numbers

n = int(input("Enter a number: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(f"Sum of first {n} natural numbers = {total}")
