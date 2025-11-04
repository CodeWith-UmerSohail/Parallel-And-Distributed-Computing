import threading
import time
import random

# Barrier for 4 threads
barrier = threading.Barrier(4)

def worker(num):
    print(f"Worker {num} starting step 1")
    time.sleep(random.uniform(1, 2))
    
    print(f"Worker {num} reached first barrier")
    barrier.wait()  # First barrier
    print(f"Worker {num} passed first barrier")

    print(f"Worker {num} starting step 2")
    time.sleep(random.uniform(1, 2))
    
    print(f"Worker {num} reached second barrier")
    barrier.wait()  # Second barrier
    print(f"Worker {num} passed second barrier")

# Create 4 threads
threads = [threading.Thread(target=worker, args=(i,)) for i in range(4)]

# Start and join threads
for t in threads: t.start()
for t in threads: t.join()

print("All workers finished!")
