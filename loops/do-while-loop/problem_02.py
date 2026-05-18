# Multiplication table using do-while logic

num = int(input("Enter a number: "))

i = 1

while True:
    print(num, "x", i, "=", num * i)

    i += 1

    if i > 10:
        break
