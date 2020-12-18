import sys
import re

inner_bracket_re = re.compile(r'(\([^())]*\))')

def Evaluate(expression):
  while '(' in expression:
    expression = inner_bracket_re.sub(lambda m: Evaluate(m.group(1)[1:-1]), expression)
  tokens = re.findall('[0-9]+|\S', expression.strip())
  accum, tokens = int(tokens[0]), tokens[1:]
  while len(tokens):
    op, val, tokens = tokens[0], tokens[1], tokens[2:]
    accum = eval(f'{accum}{op}{val}')
  return str(accum)

print(sum(int(Evaluate(line)) for line in sys.stdin))
