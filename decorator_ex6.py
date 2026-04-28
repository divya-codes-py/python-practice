import random

def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"⚠️ Attempt {attempt} failed: {e}")
            print(f"❌ Failed after {n} attempts!")
        return wrapper
    return decorator

@retry(3)
def risky_function():
    if random.random() < 0.7:
        raise Exception("Something went wrong!")
    print("✅ Success!")

risky_function()
