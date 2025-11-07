# gather.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

my_value = rank ** 2  # each process sends its square
result = comm.gather(my_value, root=0)

if rank == 0:
    print("Squares collected from all ranks:", result)