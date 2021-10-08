'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

https://leetcode.com/problems/maximum-subarray/
https://www.youtube.com/watch?v=58yMrWfUS7k&ab_channel=thecodingworld
'''

# below method is using kadan's algorithm.
def maxSubArray(nums):
    total_sum = max_sum = nums[0]

    for i in nums[1:]:
        total_sum= max(i, total_sum+i)
        max_sum = max(max_sum, total_sum)

    return max_sum

n = [-2,1,-3,4,-1,2,1,-5,4]

print(maxSubArray(n))

# Another Solution
def maxSubArray(A):
    s=0
    m=A[0]
    for i in A:
        s+=i
        m=max(s,m)
        if s<0:
            s=0
    return m
A = [1, 2, 3, 4, -10]
print(maxSubArray(A))
