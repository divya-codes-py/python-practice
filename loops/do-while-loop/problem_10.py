# Fibonacci series using do-while logic

n = int(input("Enter number of terms: "))

a = 0
b = 1
count = 1

while True:
    print(a, end=" ")

    c = a + b
    a = b
    b = c

    count += 1

    if count > n:
        break
