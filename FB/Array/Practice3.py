def containsDuplicate(nums):
    return not (len(nums) == len(set(nums)))

x= [2,14,18,22,22]
print(containsDuplicate(x))

