# thread_ex5.py

import threading
import queue
import time

def producer(q):
    for i in range(1, 6):
        print(f"📦 Produced: {i}")
        q.put(i)
        time.sleep(0.5)
    q.put(None)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"✅ Consumed: {item}")
        time.sleep(1)

q = queue.Queue()

prod_thread = threading.Thread(target=producer, args=(q,))
cons_thread = threading.Thread(target=consumer, args=(q,))

prod_thread.start()
cons_thread.start()

prod_thread.join()
cons_thread.join()

print("🎉 Producer Consumer complete!")
