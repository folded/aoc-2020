import sys
import collections

numbers = list(map(int, sys.stdin.readline().split(',')))
mem = collections.defaultdict(collections.deque)

for i in range(30000000):
  if len(numbers):
    x, numbers = numbers[0], numbers[1:]
    mem[x].append(i)
  else:
    if len(mem[x]) == 1:
      x = 0
    else:
      x = mem[x][1] - mem[x][0]
  mem[x].append(i)
  if len(mem[x]) > 2:
    mem[x].popleft()

print(x)