s = 'abccbd'


l = ''

for i in range(len(s)):
    if s[i] not in l  :
        l+=s[i]

print(l)
