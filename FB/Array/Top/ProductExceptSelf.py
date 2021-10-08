'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

https://leetcode.com/problems/product-of-array-except-self/
'''

def productExceptSelf(nums):
    res = [1]*len(nums) # [1,1,1,1] = [1,2,
    left = 1  # 2
    for i in range(len(nums)):
        res[i] *=left
        left*=nums[i]
        # print(f"result-{res}, left--{left}")
    print(res)

    right = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= right
        right *= nums[i]
        print(f"result-{res}, right--{right}")
    return res



nums = [2,3,4,5]

# print(productExceptSelf(nums))



# Another method
def Test(nums):
    total = 1
    res = []
    for j in nums:
        total *= j
    for i in nums:
        res.append(int(total/i))

    return res

print(Test([1,2,3,4]))