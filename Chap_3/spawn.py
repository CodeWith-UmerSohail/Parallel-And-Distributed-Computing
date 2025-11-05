import multiprocessing
import time
import random

def upload_file(file_id):
    print(f"[Uploader {file_id}] Starting upload...")
    upload_time = random.randint(1, 4)
    time.sleep(upload_time)
    print(f"[Uploader {file_id}] Upload completed in {upload_time} seconds.\n")

if __name__ == '__main__':
    uploaders = []
    for i in range(4):
        process = multiprocessing.Process(target=upload_file, args=(i + 1,))
        uploaders.append(process)
        process.start()

    for process in uploaders:
        process.join()

    print("All uploads completed successfully!")
# Explanation:
# Five download processes start in parallel.

# Each simulates a random download time between 2–5 seconds.

# The main program waits for all to finish before printing the final message.