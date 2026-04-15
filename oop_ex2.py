class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"✅ ₹{amount} deposit aythu!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Balance saakagilla!")
        else:
            self.balance -= amount
            print(f"✅ ₹{amount} withdraw aythu!")

    def show_balance(self):
        print(f"💰 {self.owner} balance: ₹{self.balance}")

account = BankAccount("Divya", 10000)
account.show_balance()
account.deposit(5000)
account.withdraw(3000)
account.withdraw(20000)
account.show_balance()
