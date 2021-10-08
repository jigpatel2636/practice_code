'''
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

https://www.youtube.com/watch?v=SwPXgTiv8Ag&ab_channel=KnowledgeCenter
'''

def addBinary(a,b):
    result = ''
    i,j,carry = len(a)-1, len(b)-1, 0

    while i >=0 or j >=0 :
        sum = carry
        if i >=0: sum += int(a[i])
        if j >=0: sum += int(b[j])
        i, j = i-1, j-1
        carry =1 if sum>1 else 0
        result += str(sum%2)
    if carry != 0:
        result += str(carry)
    return result[::-1]

a = '11'
b = '1'
print(addBinary(a,b))