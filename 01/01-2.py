import sys

data = sorted(map(int, sys.stdin.readlines()))
vals = set(data)

for i in range(len(data)):
  for j in range(i+1, len(data)):
    v1, v2 = data[i], data[j]
    if v1 + v2 >= 2020: break
    v3 = 2020 - v1 - v2
    if v3 not in vals: continue
    print(v1,v2,v3,v1+v2+v3,v1*v2*v3)
    sys.exit(0)