def isPalindrome(s):
    s1 = ''
    for i in s:
        if i.isalnum():
            s1 += i.lower()
    print(s1)
    if s1 == s1[::-1]:
        return True
    else:
        return False


x  = "A man, a plan, a canal: Panama"

print(isPalindrome(x))