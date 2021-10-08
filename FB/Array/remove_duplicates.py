def removeDuplicates(nums):
    n = len(nums)

    if n <=1: return n

    i = j = 1
    while i < n:
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j+=1
        i+=1
    return j



x = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(x))