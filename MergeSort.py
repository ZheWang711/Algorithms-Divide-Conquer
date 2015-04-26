__author__ = 'WangZhe'


def MergeSort(inputList):
    n = len(inputList)
    if n == 1:
        return inputList
    a = inputList[0: n//2]
    b = inputList[n//2:]
    a = MergeSort(a)
    b = MergeSort(b)
    # Merge operation: The minimum element that haven't been looked at
    #  in list a and b has to be the front of the two lists,
    # The smaller one should be copy on the current first of the result list c[k]
    i = j = 0
    c = list()
    for k in range(n):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
            if i == n//2:
                for k1 in range(k+1, n):
                    c.append(b[j])
                    j += 1
                break
        else:
            c.append(b[j])
            j += 1
            if j == n-n//2:
                for k1 in range(k+1, n):
                    c.append(a[i])
                    i += 1
                break
    return c


x = [1, 2, 3, 6, 7, 5, 99, 0, -1]
y = MergeSort(x)
print(y)
