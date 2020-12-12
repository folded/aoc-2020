import numpy as np
import numpy.ma as ma
import scipy.ndimage

import sys

def ComputeNeighbours(seat_mask):
  seat_coords = set(map(tuple, np.argwhere(seat_mask)))
  seat_neighbours = {}
  for seat in seat_coords:
    neighbours = []
    for dy, dx in ((1,0), (1,1), (0,1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)):
      for dist in range(1, max(*seat_mask.shape)):
        test = (seat[0] + dy * dist, seat[1] + dx * dist)
        if test in seat_coords:
          neighbours.append(test)
          break
    seat_neighbours[seat] = tuple(zip(*neighbours))
  return seat_neighbours

plan = np.array([ list(line.strip()) for line in sys.stdin ])
seat_mask = plan == 'L'
occupied = np.zeros_like(seat_mask)

seat_neighbours = ComputeNeighbours(seat_mask)

def Update(occupied, seat_mask, seat_neighbours):
  neighbours = np.zeros_like(occupied, dtype=int)
  for seat, positions in seat_neighbours.items():
    neighbours[seat] = occupied[positions].sum()

  new_occupied = (1 - occupied) * (neighbours == 0)
  new_unoccupied = occupied * (neighbours >= 5).astype(int)

  occupied = occupied | new_occupied
  occupied = occupied & ~new_unoccupied
  occupied = occupied & seat_mask

  return occupied

while True:
  last = occupied
  occupied = Update(occupied, seat_mask, seat_neighbours)

  if (last == occupied).all():
    print(occupied.sum())
    break