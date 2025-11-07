# scatter.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

info = None
if rank == 0:
    info = ["apple", "banana", "cherry", "date"]

received = comm.scatter(info, root=0)
print(f"Process {rank} received: {received}")

scatter.py