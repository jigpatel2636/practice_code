def plusOne(A):
    z = ''
    for i in A:
        z += str(i)
    x = int(z) + 1
    lst = []
    for j in str(x):
        lst.append(j)
    return lst


A = [1,2,3]
print(plusOne(A))