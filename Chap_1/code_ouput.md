## 🧵 Thread Synchronization (Multithreading vs Multiprocessing)

This experiment compares **Multithreading** and **Multiprocessing** performance.

### 🔹 Summary
- **Multithreading**: Slower due to thread synchronization and GIL (Global Interpreter Lock).  
- **Multiprocessing**: Faster because it runs processes in parallel using multiple CPU cores.

### ⚙️ Results
| Workers | Multiprocessing (sec) | Multithreading (sec) |
|----------|-----------------------|----------------------|
| 5        | 2.79                  | 6.39                 |
| 10       | 6.27                  | 12.95                |
| 15       | 8.32                  | 19.06                |

✅ **Multiprocessing performs better** for CPU-bound tasks.

### 📸 Output Screenshot
![Output](03da9ada-9f2e-4996-9fa9-9757eddead2f.png)

