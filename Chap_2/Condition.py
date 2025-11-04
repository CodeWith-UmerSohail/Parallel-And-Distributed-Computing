import threading
import time

condition = threading.Condition()
green_light = False

def car():
    with condition:
        print("Car waiting for green light...")
        condition.wait_for(lambda: green_light)
        print("Car passed the signal!")

def traffic_signal():
    global green_light
    time.sleep(3)
    with condition:
        green_light = True
        print("Signal turned GREEN! Cars can go.")
        condition.notify_all()

# Start threads
threading.Thread(target=car).start()
threading.Thread(target=traffic_signal).start()
