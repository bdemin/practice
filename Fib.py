def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# for i in range(10):
    # print(fib(i))


def better_fib(n, mem = {0: 0, 1: 1}):
    if n not in mem:
        mem[n] = (better_fib(n-1, mem) + better_fib(n-2, mem))    
    return mem[n]

# for i in range(10):
    # print(better_fib(i))

# print(better_fib(100))

def lut_fib(n):
    if n < 2:
        return n
    lut = [0, 1]
    for i in range(2, n + 1):
        lut.append(lut[i-1] + lut[i-2])
    return lut[n]

# for i in range(10):
    # print(lut_fib(i))


def even_better_fib(n, mem = [0, 1]):
    if len(mem) < n:
        mem.append(even_better_fib(n-1, mem) + even_better_fib(n-2, mem))
    return mem[n]

# a=2
# print(even_better_fib(a))

import numpy as np 

def test(n, mem = np.zeros(n)):
    if n