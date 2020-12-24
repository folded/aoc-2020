import sys
import re
import numpy as np
import collections

# ne, nw, e, w, se, sw
delta = {
  'nw': np.array((0,+1)),
  'ne': np.array((+1,+1)),
  'w': np.array((-1,0)),
  'e': np.array((+1,0)),
  'sw': np.array((-1,-1)),
  'se': np.array((0,-1)),
}

tiles = collections.Counter()

for line in sys.stdin:
  pos = np.array((0,0))
  for step in re.findall(r'ne|nw|e|w|se|sw', line):
    pos += delta[step]
  tiles[tuple(pos)] += 1

print(len([ pos for pos,count in tiles.items() if count % 2]))