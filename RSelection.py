__author__ = 'WangZhe'
import random
# File: RSelection.py
# Description:
#   This file contains a randomized selection algorithm,
#   which could solve the problem of "output the ith smallest element in the unsorted array"
#   This algorithm is derived from quick sort
# Algorithm pseudo code:
#   RSelection(arr, i, n)   # n is the length of arr
#       1. if n == 1    return arr[0]
#       2. j = the index of the pivot ( partition procedure, whose running time is O(n) )
#       3. if i == j    return arr[n]
#       4. if j < j     return RSelection(left part of arr, i, length of left part of arr)
#       5. if j > i     return RSelection(right part of arr, i - length of left arr - 1, length of right part arr)
#
#
#   Attention:
#       in this version of implementation,
#       j refers to the global index of the pivot (no offset in the recursive calls)
#       i refers to the index of goal element in the sorted array

def partition(arr, l, r):
    ran = random.randrange(l, r)
    arr[l], arr[ran] = arr[ran], arr[l]
    pivot = arr[l]
    j = l+1
    for i in range(l+1, r+1):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[l], arr[j-1] = arr[j-1], arr[l]
    return j-1


def RSelection(arr, l, i, n):   # l is the left hand of arr, n is the length, thus the right hand is  n+l-1
    if n == 1:
        return arr[l]
    j = partition(arr, l, n+l-1)
    if i == j:
        return arr[j]
    if i < j:
        return RSelection(arr, l, i, j-l)
    if i > j:
        return RSelection(arr, j+1, i, n+l-j-1)


# test case
n = 100
l = [i for i in range(n)]
for i in range(n):
    a = random.randrange(0, n)
    b = random.randrange(0, n)
    l[a], l[b] = l[b], l[a]
print(l)

for i in range(n//10):
    a = RSelection(l,0,i,len(l))
    print(a)
    print(l)