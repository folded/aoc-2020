import sys
import collections
import numpy as np

target = 69316178

vals = np.array(list(map(int, sys.stdin)))

i, j, s = 0, 0, 0

while s != target:
  if s < target:
    s += vals[j]
    j += 1
  elif s > target:
    s -= vals[i]
    i += 1

print(min(vals[i:j]) + max(vals[i:j]))