import sys
import numpy as np

M = 1000000
pnext = np.zeros(M, int)
pprev = np.zeros(M, int)

pnext[:-1] = np.arange(1, M)
pnext[-1] = 0

pprev[1:] = np.arange(0, M - 1)
pprev[0] = M - 1

state = np.array(list(map(int, list(sys.stdin.readline().strip())))) - 1

for i in range(1, len(state)):
  pnext[state[i-1]] = state[i]
  pprev[state[i]] = state[i-1]

if len(state) < M:
  pnext[state[-1]] = len(state)
  pprev[len(state)] = state[-1]
  pprev[state[0]] = M - 1
  pnext[M - 1] = state[0]
else:
  pnext[state[-1]] = state[0]
  pprev[state[0]] = state[-1]

idx = state[0]

for i in range(10 * M):
  splice_start = pnext[idx]
  splice_mid = pnext[splice_start]
  splice_end = pnext[splice_mid]

  pnext[idx] = pnext[splice_end]
  pprev[pnext[splice_end]] = idx

  insert = idx - 1
  if insert < 0: insert = M - 1

  while insert in (splice_start, splice_mid, splice_end):
    insert -= 1
    if insert < 0: insert = M - 1

  insert_next = pnext[insert]

  pprev[splice_start] = insert
  pnext[insert] = splice_start

  pnext[splice_end] = insert_next
  pprev[insert_next] = splice_end

  idx = pnext[idx]

a = pnext[0]
b = pnext[a]

print((a+1)*(b+1))