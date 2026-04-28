def validate_args(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                print(f"❌ Negative numbers not allowed! Got: {arg}")
                return
        return func(*args, **kwargs)
    return wrapper

@validate_args
def add(a, b):
    result = a + b
    print(f"✅ {a} + {b} = {result}")

@validate_args
def multiply(a, b):
    result = a * b
    print(f"✅ {a} x {b} = {result}")

add(5, 3)
add(-2, 3)
multiply(4, 5)
multiply(4, -5)
