def range_generator(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step

print("range_generator(0, 20, 3):")
for num in range_generator(0, 20, 3):
    print(num, end=" ")

print("\n\nrange_generator(1, 10, 2):")
for num in range_generator(1, 10, 2):
    print(num, end=" ")
