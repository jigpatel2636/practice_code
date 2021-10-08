lst = [10,15,4,23,0]

for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i],lst[j] = lst[j], lst[i]

print(lst)