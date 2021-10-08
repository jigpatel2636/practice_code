# https://leetcode.com/problems/roman-to-integer
"""
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
"""
d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
# x = 'XLIX' ---> 49
s = input("Enter a Roman number: ")

current = 0
prev = 0
total = 0

for i in range(len(s)):
    if d[s[i]] > prev:
        current = d[s[i]]
        total = total + (current - 2*prev)
    else:
        total += current
    prev = current

print(total)