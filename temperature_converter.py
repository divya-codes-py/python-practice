print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("\nChoose option: ")

if choice == "1":
    celsius = float(input("Enter temperature: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

elif choice == "2":
    fahrenheit = float(input("Enter temperature: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius}°C")

else:
    print("Wrong option!")
