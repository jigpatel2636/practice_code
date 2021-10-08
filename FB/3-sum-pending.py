# Big O(n^3)
S = [-1, 0, 1, 2, -1 -4]
# target = 0
# for i in range(len(S)):
#     for j in range(i+1, len(S)):
#         for k in range(j+1, len(S)):
#             if S[i]+S[j]+S[k] == target:
#                 print([i, j, k])


# Big O(n^2)

def ThreeSum(nums):
    nums.sort()
    res = []

    for i in range(len(nums)-2):
        if nums[i] > 0:
            break
        if nums[i] == nums[i-1] and i > 0:
            continue
        lower = i+1
        upper = len(nums) - 1

        while lower < upper:
            s = nums[i] + nums[lower] + nums[upper]

            if s == 0:
                res.append((nums[i], nums[lower], nums[upper]))
            if s<=0:
                lower+= 1
                while (nums[lower] == nums[lower-1]) and lower < upper:
                    lower+=1

            else:
                upper -= 1
    return res

print(ThreeSum(S))