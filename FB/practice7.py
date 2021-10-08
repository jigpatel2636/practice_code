'''
Rearrange a string in sorted order followed by the integer sum
Difficulty Level : Easy
 Last Updated : 20 Nov, 2019
Given a string containing uppercase alphabets and integer digits (from 0 to 9), the task is to print the alphabets in the order followed by the sum of digits.

Examples:

Input : AC2BEW3
Output : ABCEW5
Alphabets in the lexicographic order
followed by the sum of integers(2 and 3).
'''
import re

x = 'AC2BEW3'
lst = []
total = 0
for char in x:
    if char.isalpha():
        lst.append(char)
    else:
        total += int(char)

y = sorted(lst)
z = str(total)
y.append(z)
print("".join(y))



