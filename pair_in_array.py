import numpy as np


def pair2sum_1(arr, num):
    length = len(arr)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if arr[i] + arr[j] == num:
                print(arr[i], arr[j])
    print('Done')


def pair2sum_2(arr, num):
    length = len(arr)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if arr[i] + arr[j] == num:
                print(arr[i], arr[j])
    print('Done')

# def sum_array(arr, num, length):
#     temp = num - arr[0]
#     if arr[1] == temp:
#         return temp, arr[1]
#     else:
#         sum_array(arr[])



arr = np.random.randint(10, size = 10)
num = 10

print(arr)
pair2sum_1(arr, num)