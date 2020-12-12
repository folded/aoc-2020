import sys
import collections

preamble = int(sys.argv[1])

sums = collections.Counter()
vals = list(map(int, sys.stdin))

for i, v in enumerate(vals):
  if i >= preamble:
    if sums[v] <= 0:
      print(v)
      sys.exit(0)
    for j in range(i-preamble+1, i):
      sums[vals[i-preamble]+vals[j]] -= 1
  for j in range(max(0, i-preamble+1), i):
    sums[vals[j]+v] += 1
