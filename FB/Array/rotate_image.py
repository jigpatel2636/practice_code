"https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/"

def rotage(matrix):

    n = len(matrix[0])

    for row in range(n):
        for col in range(row, n):
            matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]


    for row in range(n):
        matrix[row].reverse()

    return matrix


x = [[5,1,9,11],
     [2,4,8,10],
     [13,3,6,7],
     [15,14,12,16]]

y = [[1]]

z = [[1,2],
     [3,4]]

print(rotage(x))
print(rotage(y))
print(rotage(z))