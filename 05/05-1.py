import sys
import string

trans = str.maketrans('FBLR', '0101')

def Decode(code):
  return int(code.translate(trans), 2)

print(max(Decode(row) for row in sys.stdin))
