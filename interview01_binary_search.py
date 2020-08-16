# challenge 01 :  binary search


def binarysearch(arr, val):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low+(high-low)//2
        if arr[mid]==val:
            return "val found at : " + str(mid+1)
        elif arr[mid] < val:
            low = mid+1
        else:
            high = mid-1

    return "value not found"


arr = [2,3,5,7,8,12,34,57,78]
val = 4
print(binarysearch(arr,val))




