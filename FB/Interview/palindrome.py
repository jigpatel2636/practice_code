'''
Write a function that returns whether a given string, ignoring punctuation and capitalization, is a palindrome. This should be done in place (without modifying/copying the string).
'''


def isPalindrome(self, s: str) -> bool:
    i, j = 0, len(s) - 1

    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True