import sys
import collections
import re
import itertools

lines = collections.deque(sys.stdin.readlines())

constraint_re = re.compile(r'([^:]*): (\d+)-(\d+) or (\d+)-(\d+)')
constraints = {}

while len(lines):
  m = constraint_re.match(lines[0])
  if m is None: break
  lo1, hi1, lo2, hi2 = map(int, m.groups()[1:])
  constraints[m.group(1)] = ((lo1, hi1), (lo2, hi2))
  lines.popleft()

while lines[0] != 'your ticket:\n': lines.popleft()
lines.popleft()
your_ticket = tuple(map(int, lines.popleft().split(',')))

while lines[0] != 'nearby tickets:\n': lines.popleft()
lines.popleft()
nearby_tickets = [ tuple(map(int, line.split(','))) for line in lines ]

s = 0

for ticket in nearby_tickets:
  for val in ticket:
    satisfied = False
    for constraint in constraints.values():
      for r in constraint:
        if r[0] <= val <= r[1]:
          satisfied = True
          break
      if satisfied:
        break
    if not satisfied:
      s += val

print(s)
    