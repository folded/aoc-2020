import sys
import itertools
import collections

def ReadRecord(it):
  return list(itertools.takewhile(lambda x: x.strip(), it))

def Records():
  lines = iter(sys.stdin)

  while True:
    record = ReadRecord(iter(sys.stdin))
    if not len(record): return
    yield set(''.join(map(lambda x: x.strip(), record)))

print(sum(map(len, Records())))