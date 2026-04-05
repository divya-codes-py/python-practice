n = int(input("Enter how many numbers: "))

a = 0
b = 1

print("Fibonacci Series: ", end="")

for i in range(n):
    print(a, end=" ")
    next_num = a + b
    a = b
    b = next_num
