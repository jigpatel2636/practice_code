# 5 = 5X4X3X2X1
from functools import lru_cache
import sys


@lru_cache(maxsize=2000)
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

print(fact(100))



#  OR

def factoria(x):
    f = 1
    for i in range(1, x+1):
        f = f * i
    return f

print(factoria(5))


