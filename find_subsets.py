import numpy as np


def find_subsets(arr, _sum):
    return rec(arr, _sum, len(arr)-1)


def rec(arr, _sum, index):
    if _sum == 0:
        return 1
    elif _sum < 0:
        return 0
    elif index < 0:
        return 0
    elif _sum < arr[index]:
        return rec(arr, _sum, index-1)
    else:
        return rec(arr, _sum - arr[index], index-1) + rec(arr, _sum, index-1)



arr = [1, 3, 5, 7, 8]
_sum = 9
print(find_subsets(arr, _sum))