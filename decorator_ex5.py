def cache(func):
    stored = {}
    def wrapper(n):
        if n in stored:
            print(f"📦 Cache inda: fibonacci({n})")
            return stored[n]
        result = func(n)
        stored[n] = result
        return result
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"fibonacci(10) = {fibonacci(10)}")
print(f"fibonacci(8) = {fibonacci(8)}")
print(f"fibonacci(10) = {fibonacci(10)}")
