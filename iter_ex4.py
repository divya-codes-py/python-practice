def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1

gen = natural_numbers()

print("First 10 natural numbers:")
for _ in range(10):
    print(next(gen), end=" ")
