import numpy as np
import sys

trees = np.array([ list(x.rstrip()) for x in sys.stdin.readlines() ]) == '#'

row = np.arange(0, trees.shape[0])
col = (row * 3) % trees.shape[1]

print(trees[row,col].sum())