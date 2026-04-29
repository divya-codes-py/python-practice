import threading
import time

def countdown(n):
    print("⏳ Countdown start!")
    for i in range(n, -1, -1):
        print(f"   🕐 {i}")
        time.sleep(1)
    print("🔔 Time up!")

thread = threading.Thread(target=countdown, args=(5,))
thread.start()

print("✅ Main program continue aaguttide...")
thread.join()
print("✅ Countdown complete!")
