import threading
import time
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(threadName)s: %(message)s')

start_event = threading.Event()

def car(name):
    logging.info(f"{name} is ready and waiting for the green light...")
    start_event.wait()  # wait until controller gives signal
    logging.info(f"{name} started racing! 🏁")
    time.sleep(random.uniform(2, 5))
    logging.info(f"{name} finished the race!")

def race_controller():
    logging.info("Controller preparing race...")
    time.sleep(3)
    logging.info("🚦 GREEN LIGHT! Race started!")
    start_event.set()  # signal all cars to start

cars = [threading.Thread(target=car, args=(f"Car-{i}",)) for i in range(1, 4)]
controller = threading.Thread(target=race_controller, name="Controller")

controller.start()
for c in cars:
    c.start()

controller.join()
for c in cars:
    c.join()