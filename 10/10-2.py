import sys
import numpy as np

jolts = np.array([0] + sorted(map(int, sys.stdin)))
jolts = np.concatenate([jolts, [max(jolts)+3]])
N = jolts.shape[0]
ways = np.zeros(N)

ways[0] = 1

for i in range(1, N):
  for j in range(i - 1, -1, -1):
    if jolts[j] + 3 >= jolts[i]:
      ways[i] += ways[j]

print(ways[N-1])