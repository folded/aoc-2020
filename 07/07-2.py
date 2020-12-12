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

def CountContainedBags(bag):
  result = 0
  for count, inner in data.get(bag, []):
    result += count * (1 + CountContainedBags(inner))
  return result

data = dict(map(ParseContainmentDef, sys.stdin))

print(CountContainedBags('shiny gold'))