import sys
import time

import numpy as np

# l = range(1000)
# print(sys.getsizeof(5)*len(l))

# array = np.arange(1000)
# print(array.size*array.itemsize)

SIZE = 100000000
l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# python list
start = time.time()
result = [ (x+y) for x,y in zip(l1,l2)]
print("python list took: " (time.time())- start*1000)

# python numpy
start = time.time()
result = a1 + a2
print("python numpy took: " (time.time())- start*1000)


