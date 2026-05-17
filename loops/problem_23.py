# Problem 23: Print numbers between a and b divisible by 7

a = int(input("Enter start number: "))
b = int(input("Enter end number: "))
i = a
while i <= b:
    if i % 7 == 0:
        print(i, end=" ")
    i += 1
print()
