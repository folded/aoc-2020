import sys

pk1 = int(sys.stdin.readline())
pk2 = int(sys.stdin.readline())

def Gen(subject):
  p = 1
  while True:
    yield p
    p *= subject
    p %= 20201227

def Filt():
  for i, v in enumerate(Gen(7)):
    if v == pk1: yield pk2, i

def Nth(n, subject):
  for i, v in enumerate(Gen(subject)):
    if i == n:
      return v

subj, count = next(Filt())

print(Nth(count, subj))
