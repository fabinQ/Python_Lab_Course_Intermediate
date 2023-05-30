import functools
import time

start = time.time()

@functools.lru_cache(100)
def fib(n):
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)
    return result

for i in range(11):
    result = fib(i)
    print('{0:2d}  {1}, time = {2:10.5f}'.format(i, result, time.time() - start))

# print(fib.cache_info())

stop = time.time()
print("Czas wykonania programu to {} sekund".format(stop-start))
