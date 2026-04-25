numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

result = [n ** 2 if n > 0 else abs(n) for n in numbers]
print(f"Original: {numbers}")
print(f"Result:   {result}")
