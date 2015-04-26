__author__ = 'WangZhe'
# File: quicksort.py
# Description: implement the quick sort algorithm, which is in low memory cost and have small constant factor.


def partition(arr, l, r):
    p = arr[l]
    i = l + 1
    for j in range(l+1, r+1, 1):
        if arr[j] < p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i-1], arr[l] = arr[l], arr[i-1]
    return i-1


def quicksort(arr, l, r):
    if l >= r:
        return
    else:
        pivot = partition(arr, l, r)
        quicksort(arr, l, pivot-1)
        quicksort(arr, pivot+1, r)




arr = [3,8,2,5,1,4,7,6]
quicksort(arr, 0, len(arr)-1)
print(arr)