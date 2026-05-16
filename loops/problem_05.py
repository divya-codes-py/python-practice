# Problem 5: Multiplication table of n (n×1 to n×10)

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1
