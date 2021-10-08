def pattern(n):
    for i in range(1,n+1):
        for j in range(1, i+1):
            print(j, end='')
        print()


def pattern1(n):
    x = n
    for i in range(1,n +1):
        for j in range(1, x+1):
            print(j, end='')
        x -=1
        print()

# pattern1(5)

def pattern2(n):
    for row in range(n):
        for col in range(n):
            if col == 0 or row == (n-1) or row==col:
                print('*', end='')
            else:
                print(end=" ")
        print()

# pattern2(10)

def pattern3(n):
    x = n
    for row in range(n):
        for col in range(n):
            if col == n-1 or row == 0 or row == col:
                print('*', end='')
            else:
                print(end=' ')
        print()
# pattern3(10)

def pattern4(x,y):
    for row in range(1, x+1):
        for col in range(1, y+1):
            if row == 4 or row+col == 5 or col-row == 3:
                print("*", end="")
            else:
                print(end=" ")
        print()
pattern4(4,7)
