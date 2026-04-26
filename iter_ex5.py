numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def squares(nums):
    for n in nums:
        yield n ** 2

def even_squares(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

result = list(even_squares(squares(numbers)))
print(f"Original: {numbers}")
print(f"Even squares: {result}")
