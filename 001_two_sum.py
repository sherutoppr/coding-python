'''
Given an array of integer, return indices of two number such that they add up to a specific target.
you may assume that each input would have exactaly one solution
time - o(n)
space - o(n) for dictionary
'''


def twoSum(num,target):
    num_to_index = {}       # key is number , value is index
    for i, num in enumerate(num):
        if target-num in num_to_index:
            return [num_to_index[target-num],i]
        num_to_index[num] = i

    return []


num = [3,4,6,8,2,9,5]
target = 15
print(twoSum(num,target))