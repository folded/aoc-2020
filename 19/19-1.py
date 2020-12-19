import sys
import re

terminal_re = re.compile(r'"(.)"')
rule_re = re.compile(r'[0-9]+(\s+[0-9]+)*(\s*\|[0-9]+(\s+[0-9]+)*)*')

def MakeRe(rule_id, rules):
  rule = rules[rule_id]
  if isinstance(rule, str):
    return rule
  return '(' + '|'.join(f'({"".join(MakeRe(sub, rules) for sub in opt)})' for opt in rule) + ')'

rules = {}
for line in sys.stdin:
  if line.strip() == '':
    break
  rule_id, rule = line.split(':')
  m = terminal_re.search(rule)
  if m is not None:
    rule = m.group(1)
  elif rule_re.search(rule) is not None:
    rule = [ x.strip().split() for x in rule.split('|') ]
  else:
    raise RuntimeError(f'Don\'t know what to do with {repr(rule)}')
  rules[rule_id] = rule

regex = re.compile(rf'^{MakeRe("0", rules)}$')
print(len([ line for line in sys.stdin if regex.match(line) ]))
