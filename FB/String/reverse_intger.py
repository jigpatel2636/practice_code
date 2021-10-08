def reverse(nums):

    sum = 0
    sign = 1
    if nums < 0:
        sign = -1
        nums= nums*-1
    print(nums)
    while nums >0 :
        rem = nums % 10
        sum = sum * 10 + rem
        nums = nums//10

    if not -2147483648 <sum < 2147483647:
        return 0
    return sign*sum

print(reverse(-123))