import threading
import time

class SafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.RLock()

    def increment(self):
        with self.lock:
            self._change(1)

    def decrement(self):
        with self.lock:
            self._change(-1)

    def _change(self, amount):
        with self.lock:  # same thread can re-acquire lock safely
            temp = self.value
            time.sleep(0.1)
            self.value = temp + amount

def worker(counter):
    for _ in range(3):
        counter.increment()
    for _ in range(2):
        counter.decrement()

counter = SafeCounter()
threads = [threading.Thread(target=worker, args=(counter,)) for _ in range(3)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Final counter value:", counter.value)
#Explanation:
#Each thread increments and decrements the counter.
#The _change() method is called inside another locked block, so RLock is needed.
#If we used a normal Lock, this would deadlock because the same thread would try to re-acquire it.