try:
    num1 = int(input("Modala number: "))
    num2 = int(input("Eradana number: "))
    result = num1 / num2
    print(f"✅ Result: {result}")

except ZeroDivisionError:
    print("❌ Zero inda divide maadabarudu!")

except ValueError:
    print("❌ Number maatra type maadi!")
