'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
https://www.youtube.com/watch?v=jZebUENDJ1U&ab_channel=TimothyHChang
'''

# time and space complexity o(nlogn) and o(1)
# 1st Method
def findKthLargest(nums,k):

    return sorted(nums)[-k]

print(findKthLargest([3,2,1,5,6,4],2))

# 2nd Method
#time - O(nlogk), Space- O(k)
import heapq
def findKthLargest(nums, k):
    return heapq.nlargest(k,nums)[-1]

print(findKthLargest([3,2,3,1,2,4,5,5,6],4))

#3rd method
#https://www.youtube.com/watch?v=jZebUENDJ1U&ab_channel=TimothyHChang
import random
class Solution:
    def findKthLargest(self, nums,k):
        pivot = random.choice(nums)
        left = [x for x in nums if x>pivot]
        mid = [x for x in nums if x ==pivot]
        right = [x for x in nums if x < pivot]

        L,M = len(left), len(mid)

        if k <=L:
            return self.findKthLargest(left,k)
        elif k > (L+M):
            return self. findKthLargest(right, k-(L+M))
        else:
            return mid[0]

