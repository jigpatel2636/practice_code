"""
680. Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

"""
def validPalindrome(s):
    l = 0
    r = len(s) - 1

    while l < r :
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            print(l,r)
            return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]

    return True

print(validPalindrome('abc'))