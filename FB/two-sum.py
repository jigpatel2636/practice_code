# https://www.youtube.com/watch?v=2uWRxgN1Sbo&t=114s&ab_channel=OverTheShoulderCoding
# Time complexity O(n)
def twoSum(nums,target):
    compdict = dict()
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if num in compdict:
            print(compdict)
            return [compdict[num], i]
        else:
            compdict[complement] = i
    # print(compdict)

x = [2,7,11,15]
y = 9
print(twoSum(x, y))

# Time complexity 0(n^2)

def TwoSum1(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# print(TwoSum1(x, y))