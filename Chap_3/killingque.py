import multiprocessing
import time
import random

def download_file(file_name):
    print(f"[{file_name}] Download started...")
    for i in range(1, 6):
        time.sleep(random.randint(1, 3)) 
        print(f"[{file_name}] {i*20}% downloaded")
    print(f"[{file_name}] Download complete!")

if __name__ == "__main__":
    file1 = multiprocessing.Process(target=download_file, args=("File1",))
    file2 = multiprocessing.Process(target=download_file, args=("File2",))
    file3 = multiprocessing.Process(target=download_file, args=("File3",))

    file1.start()
    file2.start()
    file3.start()

    print("\nAll downloads started! Checking status...\n")
    time.sleep(2)

    print("File1 alive:", file1.is_alive())
    print("File2 alive:", file2.is_alive())
    print("File3 alive:", file3.is_alive())

    print("\nUser cancelled File2!")
    file2.terminate()   
    file2.join()        
    file1.join()
    file3.join()

    print("\nAll downloads completed or stopped!")
    print("File1 exit code:", file1.exitcode)
    print("File2 exit code:", file2.exitcode)  
    print("File3 exit code:", file3.exitcode)