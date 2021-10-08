'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1


'''
from collections import Counter
def singlNumber(nums):
    if len(nums) < 2:
        return nums[0]

    c = Counter(nums)
    tup = c.most_common().pop()
    return tup[0]

z = [4,1,2,1,2]
print(singlNumber(z))


# Another solution

def singleNumber(nums):
    if len(nums) < 2:
        return nums[0]
    dict1 = {}

    for i in nums:
        if i not in dict1:
            dict1[i] = 1
        else:
            del dict1[i]

    return list(dict1.keys())[0]

x = [4,1,2,1,2]
print(singlNumber(x))