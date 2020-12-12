import numpy as np
import sys

trees = np.array([ list(x.rstrip()) for x in sys.stdin.readlines() ]) == '#'
print(trees.shape)
def CountTrees(dy, dx):
  row = np.arange(0, trees.shape[0], dy)
  col = (row * dx // dy) % trees.shape[1]
  print(row,col)
  return trees[row,col].sum()

print(CountTrees(1,1) * CountTrees(1,3) * CountTrees(1,5) * CountTrees(1,7) * CountTrees(2,1))