# hashmap is also called dictionary, hashtable, hash, associative array
#https://www.youtube.com/watch?v=Sh2QlIKY0GU

s = 'leetcode'

d = {}
for i in range(len(s)):
    if s[i] not in d:
        d[s[i]] = 1
    else:
        d[s[i]] += 1

for i in range(len(s)):
    if d[s[i]] == 1:
        print(i)
        break
    else:
        print('-1')