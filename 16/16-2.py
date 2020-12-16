import sys
import collections
import re
import itertools
import numpy as np

def ConstraintSatisfied(v, constraint):
  return any(r[0] <= v <= r[1] for r in constraint)

def RecursivelyAssign(remaining_assignments, out):
  if not len(remaining_assignments):
    return out
  choice = min(remaining_assignments, key = lambda x: len(x[1]))
  if not len(choice[1]):
    return None
  for alt in choice[1]:
    new_out = { choice[0]: alt }
    new_out.update(out)
    r_a = [ (r[0], r[1] - {alt}) for r in remaining_assignments if r is not choice ]
    r = RecursivelyAssign(r_a, new_out)
    if r is not None:
      return r

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

s = []

for ticket in nearby_tickets:
  all_satisfied = True
  for val in ticket:
    satisfied = False
    for constraint in constraints.values():
      satisfied = ConstraintSatisfied(val, constraint)
      if satisfied:
        break
    all_satisfied &= satisfied
  s.append(all_satisfied)

valid_tickets = np.array([ ticket for ticket, valid in zip(nearby_tickets, s) if valid ])

possible_assignments = []
for col in range(valid_tickets.shape[1]):
  vals = valid_tickets[:,col].reshape(-1)
  satisfied = {
    name for name, constraint in constraints.items()
    if all(ConstraintSatisfied(val, constraint) for val in vals)
  }
  possible_assignments.append((col, satisfied))

assignments = RecursivelyAssign(possible_assignments,{})

print(np.product([ your_ticket[col] for col, name in assignments.items() if name.startswith('departure') ]))