import functools
import time
from functools import lru_cache

start = time.time()
print(start)


def mytipleText(myStr, n):
    return myStr * n

@lru_cache
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

for i in range(1000):
    factorial(i)


stop = time.time()
print(start - stop)

nums = [1,2,3,4,5]

sumNum = 0

for num in nums:
    sumNum += 0

