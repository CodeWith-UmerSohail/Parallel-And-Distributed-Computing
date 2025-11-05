import multiprocessing
import time
import random

def backup_folder(folder_name):
    process_name = multiprocessing.current_process().name
    print(f"[{process_name}] Starting backup of {folder_name}...")
    backup_time = random.randint(2, 5)
    time.sleep(backup_time)
    print(f"[{process_name}] Finished backup of {folder_name} in {backup_time} seconds.\n")

if __name__ == "__main__":
    folders = ["Documents", "Pictures", "Videos"]

    backup1 = multiprocessing.Process(name="Backup Worker 1", target=backup_folder, args=(folders[0],))
    backup2 = multiprocessing.Process(name="Backup Worker 2", target=backup_folder, args=(folders[1],))
    backup3 = multiprocessing.Process(target=backup_folder, args=(folders[2],))  # default name

    # Make the last one a daemon (runs in background)
    backup3.daemon = True

    backup1.start()
    backup2.start()
    backup3.start()

    print("\nAll backup processes started!\n")

    # Wait only for non-daemon processes
    backup1.join()
    backup2.join()

    print("Main process: essential backups completed. Exiting now...")
