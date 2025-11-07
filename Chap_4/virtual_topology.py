# virtualTopology.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()

# Create a 2x2 grid if possible
dims = [2, 2]
periods = [False, False]
cart = comm.Create_cart(dims, periods=periods, reorder=True)

rank = cart.Get_rank()
coords = cart.Get_coords(rank)

# find neighbors (up/down/left/right)
up, down = cart.Shift(0, 1)
left, right = cart.Shift(1, 1)

print(f"Rank {rank} coords {coords} | up={up}, down={down}, left={left}, right={right}")