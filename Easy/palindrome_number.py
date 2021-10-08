# if given number is integer, then convert it into string first and then do reverse.
# https://leetcode.com/problems/palindrome-number/

x = 121
y = str(x)
if y[::-1] == y:
    print("True")
else:
    print("False")