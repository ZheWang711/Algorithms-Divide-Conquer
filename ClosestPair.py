__author__ = 'WangZhe'
import math
# File ClosestPair.py
# Description: This script implement the closest pair searching algorithm,
#               which is an example of divide and conquer.
# At: in front of the door of C400
# Start: 04/09/2015 14:32
# Finish:
# After Debugging

# Function: SortByKey
#   input: P a list of points (tuples)
#   output: sorted array by key
#   using divide and conquer paradigm

def pointSortByKey(arr, key):
    n = len(arr)

    if n == 1:
        return arr
    else:
        #indexLeft = [index[i] for i in range(n//2)]
        #indexRight = [index[i + n//2] for i in range(n-n//2)]
        arrLeft = [arr[i] for i in range(n//2)]
        arrRight = [arr[i + n//2] for i in range(n-n//2)]
        arrLeft = pointSortByKey(arrLeft, key)
        arrRight = pointSortByKey(arrRight, key)
        totalArr = [0 for i in range(n)]
        i = 0
        j = 0
        for k in range(n):
            if i == n//2:
                for delta in range(n - n//2 - j):
                    totalArr[k + delta] = arrRight[j + delta]
                break
            if j == n-n//2:
                for delta in range(n//2 - i):
                    totalArr[k + delta] = arrLeft[i + delta]
                break
            if arrLeft[i][key] <= arrRight[j][key]:
                totalArr[k] = arrLeft[i]
                i += 1
            else:
                totalArr[k] = arrRight[j]
                j += 1
        return totalArr

def pointSortByX(arr):
    return pointSortByKey(arr, 0)

def pointSortByY(arr):
    return pointSortByKey(arr, 1)

# package function
def ClosestPair(pts):
    points = [(pts[i][0], pts[i][1], i) for i in range(len(pts))]
    # 1st preprocessing O(nlogn)
    Px = pointSortByX(pointSortByY(points))
    Py = pointSortByY(pointSortByX(points))

    # call the true function
    return closestpair(Px, Py)

def distence(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closestpair(Px, Py):
    n = len(Px)
    # base cases (n = 2 & n = 3)
    if n == 2:
        return Px[0], Px[1]
    if n == 3:
        p1 = Px[0]
        p2 = Px[1]
        p3 = Px[2]
        d1 = distence(p1, p2)
        d2 = distence(p1, p3)
        d3 = distence(p2, p3)
        if d1 < d2:
            if d3 < d1:
                return p2, p3
            else:
                return p1, p2
        else:
            if d3 < d2:
                return p2, p3
            else:
                return p1, p3
    #   form Qx, Qy, Rx, Ry
    nleft = n//2 + 1
    nright = n - n//2 - 1
    Qx = [Px[i] for i in range(nleft)]
    Rx = [Px[nleft + delta] for delta in range(nright)]
    middle = Px[nleft-1][0]     # middle X
    indexPx = [0 for i in range(n)]
    for i in range(n):
        indexPx[Px[i][2]] = i

    Qy = [0 for i in range(nleft)]
    Ry = [0 for i in range(nright)]
    i = j = 0
    for k in range(n):
        if i == nleft:
            for delta in range(nright - j):
                Ry[j + delta] = Py[k + delta]
            break
        if j == nright:
            for delta in range(nleft - i):
                Qy[i + delta] = Py[k + delta]
            break
        if indexPx[Py[k][2]] < nleft:
            Qy[i] = Py[k]
            i += 1
        else:
            Ry[j] = Py[k]
            j += 1
    #   (p1,q1) = closestpair(Qx, Qy)
    #       (p2, q2) = closestpair(Rx, Ry)
    #   (p3, q3) = closestsplitpair(Px, Py)
    #   return best of (p1, q1) (p2, q2) (p3, q3)
    (p1, q1) = closestpair(Qx, Qy)
    (p2, q2) = closestpair(Rx, Ry)
    d1 = distence(p1, q1)
    d2 = distence(p2, q2)
    if d1 < d2:
        smallPair = (p1, q1)
        smallD = d1
    else:
        smallPair = (p2, q2)
        smallD = d2
    pair3 = closestsplitpair(Px, Py, smallD)
    if pair3 == ((0, 0), (0, 0)):
        return smallPair
    else:
        p3, q3 = pair3
        d3 = distence(p3, q3)
        if d3 < smallD:
            smallPair = (p3, q3)
            smallD = d3
        return smallPair


def closestsplitpair(Px, Py, smallD):
    n = len(Px)
    left = n//2
    middleX = Px[left-1][0]
    Sy = [Py[i] for i in range(n) if abs(Py[i][0] - middleX) < smallD]
    best = smallD
    bestPair = ((0, 0), (0, 0))
    for i in range(0, len(Sy)-1, 1):
        for j in range(1, min(7, len(Sy)-i), 1):
            d = distence(Sy[i], Sy[i+j])
            if d < best:
                best = d
                bestPair = Sy[i], Sy[i+j]
    return bestPair

import random
#a = [(random.randint(1, 200000), random.randint(1, 200000)) for i in range(100)]
#a = [(-1, 15), (14, 1), (14, 189), (14, 84)]
a = [(-10, 10), (0, -1), (0, 1), (0, 5), (2, 3)]
print(a)
print(ClosestPair(a))



