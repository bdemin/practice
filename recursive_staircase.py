def num_ways(n):
    if n==0:
        return 1
    elif n<=2:
        return n
    else:
        return num_ways(n-1) + num_ways(n-2)


for i in range(5):
    print(num_ways(i))


X = [1, 3, 5]
def num_ways_v2(n):
    if n==0:
        return 1
    count = 0
    for steps in X:
        if steps <= n:
            count += num_ways_v2(n-steps)
    return count

for i in range(5):
    print(num_ways_v2(i))