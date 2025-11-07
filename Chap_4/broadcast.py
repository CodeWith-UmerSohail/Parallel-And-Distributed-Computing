# broadcast.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

number = None
if rank == 0:
    number = 42  # root initializes value

shared_value = comm.bcast(number, root=0)
print(f"Rank {rank} received number: {shared_value}")

broadcast.py