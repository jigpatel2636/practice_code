'''
560. Subarray Sum Equals K
Medium

7333

252

Add to List

Share
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

https://leetcode.com/problems/subarray-sum-equals-k/
https://www.youtube.com/watch?v=bqN9yB0vF08&ab_channel=thecodingworld

'''

# Approach - Using Hashmap
#{0:1, 3:1, 7:1, 14:2, 16:1, 13:1, 18:1, 20:1 }
count = 4
def subarraySum(nums, k):
    sum_dict = {0:1}
    count = 0
    sum = 0

    for num in nums:
        sum += num
        if sum-k in sum_dict:
            count += sum_dict[sum-k]
        if sum in sum_dict:
            sum_dict[sum] += 1
        else:
            sum_dict[sum] = 1
    return count

k = 7
n = [3,4,7,2,-3,1,4,2]
print(subarraySum(n, k))

