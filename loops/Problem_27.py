# Find LCM of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

largest = max(a, b)

while True:
    if largest % a == 0 and largest % b == 0:
        lcm = largest
        break
    largest += 1

print("LCM is:", lcm)
