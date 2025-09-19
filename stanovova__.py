from math import *
def f(x, p):
    if x < 20 or p > 3: return p == 3
    if p % 2 == 0:
        return f(x - 4, p + 1) or f(x - 6, p + 1) or f(ceil(x / 2), p + 1)
    else: return f(x - 4, p + 1) and f(x - 6, p + 1) and f(ceil(x / 2), p + 1)
print([s for s in range(20, 150) if f(s, 0)])