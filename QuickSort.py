import numpy as np


def QuickSort(arr, start, end):
    if start < end:
        pivot = Partition(arr, start, end)
        QuickSort(arr, start, pivot - 1)
        QuickSort(arr, pivot + 1, end)
    
    
def Partition(arr, start, end):
    pivot = arr[end]
#    i = start
    for i in range(start, end):
        if arr[i] < pivot:
            Swap(arr, start, i)
            start += 1
    Swap(arr, start, end)
    return start
            
        

def Swap(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp
    
    
arr = np.random.randint(0, 100, 10)
print(arr)
QuickSort(arr, 0, len(arr) - 1)
print(arr)