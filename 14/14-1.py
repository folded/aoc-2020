import sys
import re
import numpy as np

mem = {}

for line in sys.stdin:
  if line.startswith('mask'):
    mask = re.match(r'mask = ([X01]*)', line).group(1)
    bits = int(mask.replace('X', '0'), 2)
    mask = int(mask.replace('1', '0').replace('X', '1'), 2)
  else:
    loc, val = map(int, re.match(r'mem\[(\d+)\] = (\d+)', line).groups())
    mem[loc] = val & mask | bits

print(sum(mem.values()))