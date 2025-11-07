# deadLockProblems.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    msg = comm.recv(source=1)  # waits first
    comm.send("Reply from 0", dest=1)
    print("Process 0 finished.")

elif rank == 1:
    comm.send("Hello from 1", dest=0)
    reply = comm.recv(source=0)
    print(f"Process 1 got reply: {reply}")