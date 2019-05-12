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

for i in range(10):
    print(better_fib(i))

print(better_fib(100))