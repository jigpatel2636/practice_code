'''
227. Basic Calculator II
Medium

2365

363

Add to List

Share
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5

https://leetcode.com/problems/basic-calculator-ii/
https://www.youtube.com/watch?v=2EErQ25kKE8&t=816s&ab_channel=SaiAnishMalla

'''

def calculate(s):
    if not s:
        return 0

    stack, curr_num, operator = [], 0, '+'
    all_operator = {"+", "-", "*", "/"}
    nums = set(str(x) for x in range(10))

    for idx in range(len(s)):
        char = s[idx]
        print(char)
        if char in nums:
            curr_num = curr_num *10 + int(char)

        if char in all_operator or idx == len(s)-1:
            if operator == "+":
                stack.append(curr_num)
            elif operator == "-":
                stack.append(-curr_num)
            elif operator == "*":
                stack[-1] *= curr_num
            elif operator == "/":
                stack[-1] = int(stack[-1] / curr_num)

            curr_num = 0
            operator = char
    print(stack)
    return sum(stack)

n = "3+2*2"
print(calculate(n))