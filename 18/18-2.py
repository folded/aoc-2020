import sys
import re
import collections

# expr := add_op (* add_op)*
# add_op := bracket_expr (+ bracket_expr)*
# bracket_expr := ( expr ) | num
# num := [0-9]+

token_re = re.compile(r'[0-9]+|[+*()]')

def Tokenize(line):
  return collections.deque(token_re.findall(line))

def Bracket(tokens):
  if tokens[0] == '(':
    tokens.popleft()
    result = Expr(tokens)
    assert tokens.popleft() == ')'
    return result
  return int(tokens.popleft())

def Add(tokens):
  result = Bracket(tokens)
  while len(tokens) and tokens[0] == '+':
    tokens.popleft()
    result += Add(tokens)
  return result    

def Expr(tokens):
  result = Add(tokens)
  while len(tokens) and tokens[0] == '*':
    tokens.popleft()
    result *= Add(tokens)
  return result    

print(sum(Expr(Tokenize(line)) for line in sys.stdin))