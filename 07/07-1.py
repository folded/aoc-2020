import re
import sys
import collections

def ParseBagDef(bag_def):
  count, desc = re.match('(\d+) (\S+ \S+) bags?', bag_def).groups()
  return int(count), desc

def ParseContainmentDef(containment_def):
  bag, contents = re.match('(\S+ \S+) bags contain (.*)[.]', containment_def).groups()
  if contents == 'no other bags':
    contents = []
  else:
    contents = list(map(ParseBagDef, contents.split(', ')))
  return bag, contents

data = list(map(ParseContainmentDef, sys.stdin))

to_container = collections.defaultdict(set)

for outer_bag, contains in data:
  for count, inner_bag in contains:
    to_container[inner_bag].add(outer_bag)

visited = set()
to_visit = ['shiny gold']
while len(to_visit):
  bag = to_visit.pop()
  for outer in to_container.get(bag, []):
    if outer not in visited:
      visited.add(outer)
      to_visit.append(outer)

print(len(visited))