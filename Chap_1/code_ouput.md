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
<img width="461" height="305" alt="image" src="https://github.com/user-attachments/assets/50e4a1a5-cf4c-4d74-8cfa-840245ff980d" />


