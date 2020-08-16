'''
there are two sorted array num1 nad num2 of size m and n respectively.
find the median of two sorted array
'''
import sys


def findmediansortedarray(num1, num2):

    ls1 = len(num1)
    ls2 = len(num2)

    if ls1 < ls2:
        return FindMedianSortedArray(num2, num1)

    l = 0
    r = ls2*2
    while l <= r:

        mid2 = (l+r) >> 1
        mid1 = ls1 + ls2 - mid2
        L1 = -sys.maxsize - 1 if mid1 == 0 else num1[(mid1-1) >> 1]
        L2 = -sys.maxsize -1 if mid2 == 0 else num2[(mid2-1) >> 1]

        R1 = sys.maxsize if mid1 == 2*ls1 else num1[mid1 >> 1]
        R2 = sys.maxsize if mid2 == 2*ls2 else num2[mid2 >> 1]

        if L1 > R2:
            l = mid2 + 1
        elif L2 > R1:
            r = mid2-1
        else:
            return (max(L1, L2) + min(R1, R2))/2.0


num1 = [1,2]
num2 = [3,4]

print(findmediansortedarray(num1,num2))







