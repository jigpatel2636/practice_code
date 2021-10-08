# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# 123 % 10 --> 3 --> 3 * 10 + (12 % 10) + (1%10)
#https://www.youtube.com/watch?v=Io9ujnnR4sI

def mod(number, m):
    if number < 0:
        return number % -m
    return number % m

def divide(number, div):
    return int(number/div)

MAX_INT = 2 ** 32 -1 # 2147483647
MIN_INT = -2 ** 32 # -2147483648

def reverse_number(x):
    res = 0
    while x:
        pop = mod(x, 10)
        x = divide(x,10)
        if res > divide(MAX_INT, 10) or (res == divide(MAX_INT,10) and pop > 7):
            return 0
        if res < divide(MIN_INT, 10) or (res == divide(MIN_INT,10) and pop < -8):
            return 0
        res = res * 10 + pop
    return res

print(reverse_number(-123))