# 计算Pi
from random import *
import time

region = 10000 * 10000
hits = 0.0
start = time.perf_counter();

for i in range(region):
    x = random()
    y = random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = (hits / region) * 4
print(pi)
print(time.perf_counter() - start)