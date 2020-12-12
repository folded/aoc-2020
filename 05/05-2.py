import sys
import string

trans = str.maketrans('FBLR', '0101')

def Decode(code):
  return int(code.translate(trans), 2)

ids = { Decode(row) for row in sys.stdin }

print(list(x for x in set(range(min(ids), max(ids))) - ids if x+1 in ids and x-1 in ids))
