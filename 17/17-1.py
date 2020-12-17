import sys
import numpy as np
import scipy.ndimage

config = np.array([list(x.strip()) for x in  sys.stdin.readlines()]) == '#'

N = max(config.shape) + 12
state = np.zeros((N,N,N), dtype=int)
sz = np.array(config.shape)
xl, yl = -sz//2
xh, yh = np.array([xl, yl]) + sz

state[N//2,N//2+xl:N//2+xh,N//2+yl:N//2+yh] = config
neighbours = np.ones((3,3,3), dtype=int)
neighbours[1,1,1] = 0

for i in range(6):
  ncount = scipy.ndimage.convolve(state, neighbours, mode='constant', cval=0)
  n3 = ncount==3
  n2 = ncount==2
  state = ((n2 | n3) & state) | (n3 & ~state)

print(state.sum())