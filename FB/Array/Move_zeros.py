'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

'''

def moveZeroes(nums):

    zero_count = nums.count(0)

    next_non_zero = 0

    for i in nums:
        if i != 0 :
            nums[next_non_zero] = i
            next_non_zero += 1

    for zero in range(1, zero_count+1):
        nums[-zero] = 0

    return nums

x = [0,1,0,3,12]
print(moveZeroes(x))