def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def apply(func, numbers):
    return [func(n) for n in numbers]

numbers = [1, 2, 3, 4, 5]

print(f"Squares: {apply(square, numbers)}")
print(f"Cubes: {apply(cube, numbers)}")
