"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

# def strStr(haystack, needle):
#     if len(needle) == 0:
#         return 0
#     for i in range(len(haystack)):
#         if haystack[i: i+len(needle)] == needle:
#             return i
#     return -1
#
# z = strStr('hello', 'll')
# print(z)
#
# y = strStr('aaaaa', 'bba')
# print(y)

## Another method ##

def strStr(haystack, needle):
    return haystack.find(needle)  ## find method returns first index if match found otherwise return -1


x = strStr('hello', 'll')
print(x)