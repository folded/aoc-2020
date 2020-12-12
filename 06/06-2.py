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
    c = collections.Counter(''.join(map(lambda x: x.strip(), record)))
    yield [ k for k,v in c.items() if v == len(record) ]

print(sum(map(len, Records())))