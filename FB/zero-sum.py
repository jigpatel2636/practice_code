'''Algorithm:
Run three nested loops with loop counter i, j, k
The first loops will run from 0 to n-3 and second loop from i+1 to n-2 and the third loop from j+1 to n-1. The loop counter represents the three elements of the triplet.
Check if the sum of elements at i’th, j’th, k’th is equal to zero or not. If yes print the sum else continue.'''


x = [0, -1, 2, -3, 1]
n = len(x)
for i in range(0, n):
    # print(x[i])
    for j in range(i+1, n-1):
        # print(x[j])
        for k in range(j+1, n):
            # print(x[k])
            if (x[i] + x [j] + x[k] == 0) :
                print(x[i], x[j], x[k])
