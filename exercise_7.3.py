#!/usr/bin/env python
import math

def jiecheng(n):
    if n == 0 :
        return 1
    else:
        return n*jiecheng(n - 1)

def estimate_pi():
    total = 0
    n = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        fenzi =jiecheng(4 * n) * (26390 * n + 1103)
        fenmu = jiecheng(n)**4 * 396**(4*n)
        result = factor * fenzi / fenmu
        total = total + result
        n = n + 1
        if abs(result) < 1e-15:
            break
    return 1 / total

a = estimate_pi()
print(a)
print(math.pi)