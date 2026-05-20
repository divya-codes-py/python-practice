class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def display(self):
        print(f"Account: {self.name}")
        print(f"Balance: {self.balance}")
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposited: {amount}")
        print(f"Balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("\n❌ Insufficient funds!")
            print(f"Balance: {self.balance}")
        else:
            self.balance = self.balance - amount
            print(f"\nWithdrawn: {amount}")
            print(f"Balance: {self.balance}")

acc = BankAccount("Divya", 1000)
acc.display()
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(5000)
