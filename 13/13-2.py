import sys
import numpy as np
import itertools


start_time = int(sys.stdin.readline())
moduli = np.array([ 0 if x == 'x' else int(x) for x in sys.stdin.readline().split(',') ], dtype='int64')
remainders = np.arange(moduli.shape[0], dtype='int64')

def ExtendedGcd(a, b):
  old_r, r = a, b
  old_s, s = 1, 0
  old_t, t = 0, 1
  
  while r != 0:
    quotient = old_r // r
    old_r, r = r, old_r - quotient * r
    old_s, s = s, old_s - quotient * s
    old_t, t = t, old_t - quotient * t
  
  return old_r, old_s, old_t

gcd, a, b = ExtendedGcd(3,4)

def SolvePair(p1, p2):
  a1, n1 = p1
  a2, n2 = p2
  gcd, m1, m2 = ExtendedGcd(n1, n2)
  x = a1 * m2 * n2 + a2 * m1 * n1
  n = n1 * n2
  x = x % n
  return x, n

def SolveN(p):
  p = list(p)
  while len(p) > 1:
    p[:2] = [SolvePair(*p[:2])]
  return p[0][0]

remainders = remainders[moduli != 0]
moduli = moduli[moduli != 0]
remainders = (moduli - remainders) % moduli

prob = zip(map(int, remainders), map(int, moduli))

print(SolveN(prob))