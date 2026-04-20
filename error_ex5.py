def calculator(num1, operator, num2):
    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            raise ValueError("Invalid operator!")

    except ZeroDivisionError:
        print("❌ Zero inda divide maadabarudu!")

    except ValueError as e:
        print(f"❌ Error: {e}")

    else:
        print(f"✅ Result: {num1} {operator} {num2} = {result}")

    finally:
        print("🔢 Calculator ready!")

calculator(10, "+", 5)
calculator(10, "/", 0)
calculator(10, "%", 5)
