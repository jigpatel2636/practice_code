X = 'abcdeca'
k = 2
Y = X[::-1]
n = len(X)
m = n

L = [[0]*(n+1) for _ in range(m+1)]
print(L)

for i in range(m + 1):
    for j in range(n + 1):
        if not i or not j:
            print(i, " ", j)
            L[i][j] = 0
        elif X[i - 1] == Y[j - 1]:
            L[i][j] = L[i - 1][j - 1] + 1
        else:
            L[i][j] = max(L[i - 1][j], L[i][j - 1])

            # L[m][n] contains length
    # of LCS for X and Y
ips = L[m][n]
# print(ips)
# if (n-ips <=k):
#     print('yes')
# else:
#     print("No")


