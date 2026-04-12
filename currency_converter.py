currency_converter.py

def get_rates():
    rates = {
        "INR": 1.0,
        "USD": 0.012,
        "EUR": 0.011,
        "GBP": 0.0094,
        "JPY": 1.78,
        "AUD": 0.018,
        "CAD": 0.016,
        "SGD": 0.016,
        "AED": 0.044,
        "CNY": 0.087
    }
    return rates

def convert(amount, from_currency, to_currency, rates):
    in_inr = amount / rates[from_currency]
    result = in_inr * rates[to_currency]
    return round(result, 2)

def show_currencies(rates):
    print("\n💱 Available Currencies:")
    print("=" * 35)
    for i, currency in enumerate(rates.keys(), 1):
        print(f"  {i}. {currency}")
    print("=" * 35)

def main():
    rates = get_rates()

    print("💱 Currency Converter!")
    print("=" * 35)
    print("Note: INR base rates use maadagtide")

    while True:
        print("\n📌 Menu:")
        print("1. Currency convert maadi")
        print("2. Ella currencies nodu")
        print("3. Exit")

        choice = input("\nOption (1-3): ")

        if choice == "1":
            show_currencies(rates)

            from_cur = input("\nYaavudu currency inda convert maadali? ").upper()
            if from_cur not in rates:
                print("❌ Invalid currency!")
                continue

            to_cur = input("Yaavudu currency ge convert maadali? ").upper()
            if to_cur not in rates:
                print("❌ Invalid currency!")
                continue

            try:
                amount = float(input(f"Amount ({from_cur}): "))
                if amount <= 0:
                    print("⚠️ Amount 0 kante jaasti irali!")
                    continue
            except ValueError:
                print("⚠️ Valid number type maadi!")
                continue

            result = convert(amount, from_cur, to_cur, rates)

            print("\n" + "=" * 35)
            print(f"💰 {amount} {from_cur}")
            print(f"   = {result} {to_cur}")
            print("=" * 35)

        elif choice == "2":
            show_currencies(rates)

        elif choice == "3":
            print("👋 Bye! Happy converting! 💱")
            break

        else:
            print("⚠️ 1 to 3 maatra type maadi!")

main()
