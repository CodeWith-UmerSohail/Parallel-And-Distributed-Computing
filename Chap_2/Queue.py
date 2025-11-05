import threading
import queue
import time

orders = queue.Queue()

def waiter():
    for i in range(3):
        order = f"Order #{i+1}"
        print(f"Waiter: Placed {order}")
        orders.put(order)
        time.sleep(1)
    orders.put(None)  # signal that all orders are done

def chef():
    while True:
        order = orders.get()
        if order is None:
            print("Chef: No more orders, closing kitchen.")
            break
        print(f"Chef: Cooking {order}")
        time.sleep(2)
        print(f"Chef: Finished {order}")
        orders.task_done()

# Start both threads
threading.Thread(target=waiter).start()
threading.Thread(target=chef).start()
