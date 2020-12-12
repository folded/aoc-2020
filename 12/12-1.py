import numpy as np
import sys

pos =np.zeros(2, float)
heading = 0.

for cmd in sys.stdin:
  cmd, v = cmd[0], int(cmd[1:])
  if cmd == 'N':
    pos += np.array([0, v])
  elif cmd == 'S':
    pos -= np.array([0, v])
  elif cmd == 'E':
    pos += np.array([v, 0])
  elif cmd == 'W':
    pos -= np.array([v, 0])
  elif cmd == 'F':
    pos += v * np.array([np.cos(heading * np.pi / 180.0), np.sin(heading * np.pi / 180.0)])
  elif cmd == 'L':
    heading += v
  elif cmd == 'R':
    heading -= v

print(np.abs(pos).sum())