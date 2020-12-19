import sys
import re

terminal_re = re.compile(r'"(.)"')
rule_re = re.compile(r'[0-9]+(\s+[0-9]+)*(\s*\|[0-9]+(\s+[0-9]+)*)*')

class Terminal:
  def __init__(self, terminal):
    self.terminal = terminal

  def SubstituteIds(self, rule_map, visited):
    visited.add(self)

  def Match(self, s):
    if s.startswith(self.terminal):
      yield s[len(self.terminal):]


class Nonterminal:
  def __init__(self, children):
    self.children = children

  def SubstituteIds(self, rule_map, visited):
    if self in visited:
      return
    visited.add(self)
    self.children = [ rule_map.get(s, s) for s in self.children ]
    for child in self.children:
      child.SubstituteIds(rule_map, visited)


class Seq(Nonterminal):
  def _Match(self, s, children):
    if not len(children):
      yield s
    else:
      child, children = children[0], children[1:]
      for s2 in child.Match(s):
        yield from self._Match(s2, children)

  def Match(self, s):
    yield from self._Match(s, self.children)


class Union(Nonterminal):
  def Match(self, s):
    for child in self.children:
      yield from child.Match(s)


rules = {}


substitutions = {
  8: '42 | 42 8',
  11: '42 31 | 42 11 31'
}

for line in sys.stdin:
  if line.strip() == '':
    break
  rule_id, rule = line.split(':')
  rule_id = int(rule_id)
  rule = substitutions.get(rule_id, rule)

  m = terminal_re.search(rule)
  if m is not None:
    rule = Terminal(m.group(1))
  elif rule_re.search(rule) is not None:
    rule = [ Seq([ int(y) for y in x.strip().split() ]) for x in rule.split('|') ]
    if len(rule) == 1:
      rule = rule[0]
    else:
      rule = Union(rule)
  else:
    raise RuntimeError(f'Don\'t know what to do with {repr(rule)}')

  rules[rule_id] = rule

pattern = rules[0]

pattern.SubstituteIds(rules, set())

print(len([ line for line in sys.stdin if '' in pattern.Match(line.strip()) ]))