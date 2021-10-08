"""
https://leetcode.com/problems/longest-common-prefix/
Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings

"""

def longestCommonPrefix(s):
    if len(s) == 0:
        return ""

    min_length = len(s[0])

    for i in range(len(s)):
        min_length = min(len(s[i]), min_length)

    lcp = ''
    i = 0
    while i < min_length:
        char = s[0][i]
        for j in range(1, len(s)):
            if s[j][i] != char:
                return lcp
        lcp += char
        i += 1
    return lcp

sx = ["flower","flow","flight"]
print(longestCommonPrefix(sx))