__author__ = 'WangZhe'

# File: CountingInversions.py
# start at 04/07/2015 21:48

def CountingInversionsNMerge(arr):
    n = len(arr)
    if n == 1:
        return arr, 0
    a = n//2  # #of elem in left arr
    b = n-a   # #of elem in right arr
    (arrLeft, leftinver) = CountingInversionsNMerge(arr[0:a])
    (arrRight, rightinver) = CountingInversionsNMerge(arr[a:n])
    i=0
    j=0
    splitInversion = 0
    totalArr = [0 for k in range(n)]
    for k in range(n):

        if i == a:
            # copy all the elements of right array then exit loop
            # there is no increment in splitInversion since no elements in leftArr
            for delta in range(b-j):
                totalArr[k+delta] = arrRight[j+delta]
            break

        if j == b:
            # copy each elements of left array then exit loop
             for delta in range(a-i):
                totalArr[k+delta] = arrLeft[i+delta]
             break

        if arrLeft[i] < arrRight[j]:
            totalArr[k] = arrLeft[i]
            i += 1

        else:
            totalArr[k] = arrRight[j]
            j += 1
            splitInversion += a-i

    inversion = leftinver + rightinver + splitInversion
    return totalArr, inversion

