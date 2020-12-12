import sys
import re
import collections
from typing import Tuple

def IsValid(pos: Tuple[int, int], char:  str, password: str) -> bool:
  return (password[pos[0]-1] == char) != (password[pos[1]-1] == char)

def Parse(line):
  m = re.match(r'([0-9]+)-([0-9]+) (\S): (\S+)', line)
  lo, hi, char, password = m.groups()
  return (int(lo), int(hi)), char, password

print(sum(IsValid(*Parse(line)) for line in sys.stdin))