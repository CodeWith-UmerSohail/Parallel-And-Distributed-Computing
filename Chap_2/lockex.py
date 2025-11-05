import threading
import time

lock = threading.Lock()
balance = 0

def deposit(amount):
    global balance
    for _ in range(5):
        with lock:  # Only one thread can change balance at a time
            temp = balance
            time.sleep(0.1)
            balance = temp + amount

threads = [threading.Thread(target=deposit, args=(100,)) for _ in range(3)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Final balance:", balance)
