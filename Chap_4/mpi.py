# helloWorld_MPI.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
total = comm.Get_size()

print(f"Process [{rank}] says: Hi! There are {total} processes running.")