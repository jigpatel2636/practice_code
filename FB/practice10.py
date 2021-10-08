x = 'jigneshjigneshjigneshjigneshjignesh'

lst = []

for char in x:
    if char not in lst:
        lst.append(char)
print("".join(lst))