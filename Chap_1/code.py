import time
import multiprocessing
import threading

# 🔢 CPU-heavy function (e.g. calculate sum of squares)
def heavy_calculation(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

def run_task(task_id, n):
    heavy_calculation(n)

if __name__ == "__main__":
    sizes = [5, 10, 15]  # number of processes/threads
    workload = 10_000_000  # increase for heavier computation

    for size in sizes:
        # ---------- Multiprocessing ----------
        print(f"\n===== Running with {size} PROCESSES =====")
        jobs = []
        start_time = time.time()

        for i in range(size):
            p = multiprocessing.Process(target=run_task, args=(i, workload))
            jobs.append(p)

        for j in jobs:
            j.start()

        for j in jobs:
            j.join()

        end_time = time.time()
        print(f"Multiprocessing ({size} processes) time = {end_time - start_time:.4f} seconds")

        # ---------- Multithreading ----------
        print(f"\n===== Running with {size} THREADS =====")
        jobs = []
        start_time = time.time()

        for i in range(size):
            t = threading.Thread(target=run_task, args=(i, workload))
            jobs.append(t)

        for t in jobs:
            t.start()

        for t in jobs:
            t.join()

        end_time = time.time()
        print(f"Multithreading ({size} threads) time = {end_time - start_time:.4f} seconds\n")