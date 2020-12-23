import sys

state = tuple(map(int, list(sys.stdin.readline().strip())))

def Rotate(state, first):
  idx = state.index(first)
  return state[idx:] + state[:idx]

def Move(state):
  sel, state = state[1:4], state[:1] + state[4:]
  i = state[0] - 1
  while True:
    try:
      idx = state.index(i) + 1
      break
    except ValueError:
      i -= 1
      if i < 0: i = 9
  return state[1:idx] + sel + state[idx:] + state[:1]

for i in range(100):
  state = Move(state)

print(''.join(map(str, Rotate(state, 1)[1:])))