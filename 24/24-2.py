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

state = { pos for pos, count in tiles.items() if count % 2 }

def CountNeighbours(positions):
  neighbours = collections.Counter()
  for p in positions:
    for d in delta.values():
      neighbours[(p[0]+d[0], p[1]+d[1])] += 1
  return neighbours

for i in range(100):
  new_black = set()
  new_white = set()
  neighbours = { s: 0 for s in state }
  neighbours.update(CountNeighbours(state))
  for n, count in neighbours.items():
    if count == 2 and n not in state:
      new_black.add(n)
    elif (count == 0 or count > 2) and n in state:
      new_white.add(n)
  state = (state | new_black) - new_white

print(len(state))