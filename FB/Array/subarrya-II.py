'''
Given two unsorted arrays, find all pairs whose sum is x
Given two unsorted arrays of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.
Examples:


Input :  arr1[] = {-1, -2, 4, -6, 5, 7}
         arr2[] = {6, 3, 4, 0}
         x = 8
Output : 4 4
         5 3

Input : arr1[] = {1, 2, 4, 5, 7}
        arr2[] = {5, 6, 3, 4, 8}
        x = 9
Output : 1 8
         4 5
         5 4
'''

arr1 = [1, 2, 4, 5, 7]
arr2 = [5, 6, 3, 4, 8]
x = 9

for i in arr1:
    for j in arr2:
        if i+j == x:
            print(i, ' ',j)