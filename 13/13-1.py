import sys
import numpy as np

start_time = int(sys.stdin.readline())
bus_ids = [ int(x) for x in sys.stdin.readline().split(',') if x != 'x' ]
waits = [ i - (start_time % i) for i in bus_ids ]
idx = np.argmin(waits)

print(bus_ids[idx] * waits[idx])