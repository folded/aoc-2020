import numpy as np
import numpy.ma as ma
import scipy.ndimage

import sys

plan = np.array([ list(line.strip()) for line in sys.stdin ])
seat_mask = plan == 'L'
occupied = np.zeros_like(seat_mask)

filt = np.array([[1,1,1], [1,0,1], [1,1,1]])

while True:
  last = occupied
  neighbours = scipy.ndimage.convolve(occupied, filt, mode='constant', cval=0)
  new_occupied = (1 - occupied) * (neighbours == 0)
  new_unoccupied = occupied * (neighbours >= 4).astype(int)

  occupied = occupied | new_occupied
  occupied = occupied & ~new_unoccupied
  occupied = occupied & seat_mask

  if (last == occupied).all():
    print(occupied.sum())
    break