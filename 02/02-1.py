import sys
import re
import collections
from typing import Tuple

def IsValid(count_range: Tuple[int, int], char:  str, password: str) -> bool:
  return count_range[0] <= password.count(char) <= count_range[1]

def Parse(line):
  m = re.match(r'([0-9]+)-([0-9]+) (\S): (\S+)', line)
  lo, hi, char, password = m.groups()
  return (int(lo), int(hi)), char, password

print(sum(IsValid(*Parse(line)) for line in sys.stdin))