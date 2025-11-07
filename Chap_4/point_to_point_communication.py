# pointToPointCommunication.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    comm.send("Data packet 0→1", dest=1)
    reply = comm.recv(source=1)
    print(f"Rank 0 got reply: {reply}")

elif rank == 1:
    data = comm.recv(source=0)
    print(f"Rank 1 received: {data}")
    comm.send("Acknowledged 1→0", dest=0)