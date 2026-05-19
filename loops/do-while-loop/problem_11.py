# Find HCF using do-while logic

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

small = min(a, b)

i = 1
hcf = 1

while True:
    if a % i == 0 and b % i == 0:
        hcf = i

    i += 1

    if i > small:
        break

print("HCF is:", hcf)
