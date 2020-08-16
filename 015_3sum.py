'''Given an array nums of n integers, are
there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.'''


def threeSum(nums):
    res = []
    nums.sort()

    i = 0
    while i < len(nums):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            curr_sum = nums[i] + nums[j] + nums[k]
            if curr_sum == 0:
                res.append([nums[i], nums[j], nums[k]])
                k -= 1
                while k > j and nums[k] == nums[k + 1]:
                    k -= 1
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
            elif curr_sum > 0:
                k -= 1
                while k > j and nums[k] == nums[k + 1]:
                    k -= 1
            else:
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1

        i += 1
        while i < len(nums) - 2 and nums[i] == nums[i - 1]:
            i += 1

    return res

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))