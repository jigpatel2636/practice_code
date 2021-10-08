'''Calculate maximum value using ‘+’ or ‘*’ sign between two numbers in a string
Difficulty Level : Easy

Examples:

Input : 01231
Output :
((((0 + 1) + 2) * 3) + 1) = 10
In above manner, we get the maximum value i.e. 10

Input : 891
Output :73
As 8*9*1 = 72 and 8*9+1 = 73.So, 73 is maximum.'''

x = '891'

res = int(x[0])

for i in range(1, len(x)):
    if int(x[i]) == 0 or int(x[i]) == 1 or res < 2:
        res = res + int(x[i])
    else:
        res = res*int(x[i])

print(res)
