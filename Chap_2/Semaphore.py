import threading
import time
import random

parking_lot = threading.Semaphore(3)  # only 3 cars can park at a time

def car(name):
    print(f"{name} is trying to park...")
    with parking_lot:  # acquire a parking space
        print(f"{name} parked.")
        time.sleep(random.uniform(1, 3))
        print(f"{name} left the parking lot.")
    print(f"{name} is gone.")

cars = [threading.Thread(target=car, args=(f"Car {i+1}",)) for i in range(6)]

for c in cars:
    c.start()

for c in cars:
    c.join()
