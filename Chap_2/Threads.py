import threading
import time

def task():
    print(f"{threading.current_thread().name} starting")
    time.sleep(2)
    print(f"{threading.current_thread().name} finished")

start_time = time.time()

threads = [threading.Thread(target=task, name=f"Thread-{i}") for i in range(3)]

for t in threads: t.start()
for t in threads: t.join()

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")