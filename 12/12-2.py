import numpy as np
import sys

pos = np.array([0,0])
way = np.array([10,1])

rot = [ np.array([[ 0,-1],
                  [+1, 0]]) ]
for i in range(2):
  rot.append(np.matmul(rot[0], rot[-1]))

for cmd in sys.stdin:
  cmd, v = cmd[0], int(cmd[1:])
  if cmd == 'N':
    way += np.array([0, v])
  elif cmd == 'S':
    way -= np.array([0, v])
  elif cmd == 'E':
    way += np.array([v, 0])
  elif cmd == 'W':
    way -= np.array([v, 0])
  elif cmd == 'F':
    pos += v * way
  elif cmd == 'L':
    way = np.matmul(rot[v//90 - 1], way)
  elif cmd == 'R':
    way = np.matmul(rot[3 - v//90], way)

print(np.abs(pos).sum())