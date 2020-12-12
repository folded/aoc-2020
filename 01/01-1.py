import sys

data = sorted(map(int, sys.stdin.readlines()))

i, j = 0, len(data) - 1

while i != j:
  if data[i] + data[j] > 2020:
    j -= 1
  elif data[i] + data[j] < 2020:
    i += 1
  else:
    print(data[i], data[j], data[i]+data[j], data[i]*data[j])
    break