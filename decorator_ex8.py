import datetime

def log(func):
    def wrapper(*args, **kwargs):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{func.__name__} called with {args} at {time}\n"

        with open("function_log.txt", "a") as f:
            f.write(log_message)

        print(f"📝 Logged: {log_message.strip()}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    result = a + b
    print(f"✅ {a} + {b} = {result}")
    return result

@log
def multiply(a, b):
    result = a * b
    print(f"✅ {a} x {b} = {result}")
    return result

add(5, 3)
multiply(4, 6)
add(10, 20)
