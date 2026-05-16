# Problem 7: Sum of all even numbers from 1 up to n

n = int(input("Enter a number: "))
total = 0
i = 2
while i <= n:
    total += i
    i += 2
print(f"Sum of even numbers up to {n} = {total}")
