import sys
import re
import numpy as np

mem = {}

def Gen(mask):
  bits = []
  for i in range(36):
    if mask & (1 << i):
      bits.append(i)

  for i in range(1 << len(bits)):
    v = 0
    for j in range(len(bits)):
      if i & (1 << j):
        v |= 1 << bits[j]
    yield v

for line in sys.stdin:
  if line.startswith('mask'):
    mask = re.match(r'mask = ([X01]*)', line).group(1)
    bits = int(mask.replace('X', '0'), 2)
    mask = int(mask.replace('1', '0').replace('X', '1'), 2)
  else:
    loc, val = map(int, re.match(r'mem\[(\d+)\] = (\d+)', line).groups())
    loc |= bits
    loc &= ~mask
    for g in Gen(mask):
      mem[loc | g] = val

print(sum(mem.values()))