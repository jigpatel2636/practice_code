a = 'abc'
b = 'stuvwx'
newString = ''

i = 0
j = 0

while i < len(a) and j <len(b):
    newString+= a[i] + b[j]
    i+=1
    j+=1
print(newString)

print(i, '', j)

if i < len(a):
    newString += a[i:]
if j < len(b):
    newString += b[j:]

print(newString)
