# Problem 20: Sum of Fibonacci series up to n terms

n = int(input("Enter number of terms: "))
a, b = 0, 1
count = 0
total = 0
while count < n:
    total += a
    a, b = b, a + b
    count += 1
print(f"Sum of first {n} Fibonacci terms = {total}")
