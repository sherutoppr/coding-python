'''Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.'''


def maxSubArray(nums):
    res = float('-inf')
    mt = 0

    for curr in nums:
        if mt > 0:
            mt += curr
        else:
            mt = curr
        res = max(res, mt)
    return res


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))