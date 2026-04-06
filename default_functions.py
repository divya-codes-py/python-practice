def profile(name, city="India", age="Not provided"):
    print(f"\nHello {name}! 👋")
    print(f"City: {city}")
    print(f"Age: {age}")

name = input("Enter your name: ")
city = input("Enter your city (or press enter): ")

if city == "":
    profile(name)
else:
    profile(name, city)
