'''Count all distinct pairs with difference equal to k
Examples:

Input: arr[] = {1, 5, 3, 4, 2}, k = 3
Output: 2
There are 2 pairs with difference 3, the pairs are {1, 4} and {5, 2}

Input: arr[] = {8, 12, 16, 4, 0, 20}, k = 4
Output: 5
There are 5 pairs with difference 4, the pairs are {0, 4}, {4, 8},
{8, 12}, {12, 16} and {16, 20}
'''

arr = [1, 5, 3, 4, 2]
k = 3

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if i - j == 3 or i-j == -3:
            print((arr[i], arr[j]))