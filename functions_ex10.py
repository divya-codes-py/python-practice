def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {round(end - start, 4)} seconds")
        return result
    return wrapper

@timer
def calculate(numbers):
    total = sum(numbers)
    print(f"Sum: {total}")

calculate([1, 2, 3, 4, 5])
