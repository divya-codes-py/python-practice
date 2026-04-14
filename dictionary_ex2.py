fruits = {"apple": 50, "banana": 20, "mango": 80}

# 1. Add grape
fruits["grape"] = 60

# 2. Update banana price
fruits["banana"] = 25

# 3. Print all fruits and prices
for fruit, price in fruits.items():
    print(f"{fruit}: ₹{price}")

# 4. Check if orange exists
if "orange" in fruits:
    print("Orange is available!")
else:
    print("Orange is not availabl
