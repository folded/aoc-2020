import sys
import numpy as np

jolts = np.array([0] + sorted(map(int, sys.stdin)))
jolts = np.concatenate([jolts, [max(jolts)+3]])

delta = jolts[1:] - jolts[:-1]

print((delta == 1).sum() * (delta == 3).sum())