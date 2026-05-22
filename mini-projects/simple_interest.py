principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (years): "))

si = (principal * rate * time) / 100
total = principal + si

print("\n---- Result ----")
print(f"Principal: {principal}")
print(f"Rate: {rate}%")
print(f"Time: {time} years")
print(f"Simple Interest: {si}")
print(f"Total Amount: {total}")
