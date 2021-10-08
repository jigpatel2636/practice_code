"""
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true

"""
s = "{[]}"
stack = []
for i in range(len(s)):
    if s[i] == '(' or s[i] == '{' or s[i] == '[':
        stack.append(s[i])
    elif s[i] == ')' and stack.pop() == '(':
        print(True)
    elif s[i] == '}' and stack.pop() == '{':
        print(True)
    elif s[i] == ']' and stack.pop() == '[':
        print(True)
    else:
        print(False)
    


