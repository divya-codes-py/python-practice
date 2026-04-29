import threading

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, amount, name):
        with self.lock:
            current = self.balance
            current += amount
            self.balance = current
            print(f"✅ {name} deposited ₹{amount} — Balance: ₹{self.balance}")

account = BankAccount()

def deposit_task(name, amount, times):
    for _ in range(times):
        account.deposit(amount, name)

thread1 = threading.Thread(target=deposit_task, args=("Divya", 100, 3))
thread2 = threading.Thread(target=deposit_task, args=("Rahul", 200, 3))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"\n🏦 Final balance: ₹{account.balance}")
