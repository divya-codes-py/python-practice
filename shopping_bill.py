items = []
total = 0

while True:
    name = input("Enter item name: ")
    
    if name == "done":
        break
    
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    amount = price * quantity
    
    items.append(f"{name} x{quantity} = {amount}")
    total = total + amount

print("\n---- Your Bill ----")
for item in items:
    print(item)
print(f"Total: {total}")
