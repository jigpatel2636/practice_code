
def isValidSudoku(board):
    r, c, b = set(), set(), set()

    for i in range(9):
        for j in range(9):
            if board[i][j]!= '.':
                r_k = (i, board[i][j])
                # print(r_k)
                c_k = (j, board[i][j])
                b_k = (i//3, j//3, board[i][j])
                if (r_k in r or c_k in c or b_k in b):
                    print(False)
                r.add(r_k)
                c.add(c_k)
                b.add(b_k)
        # print(b)
    # print(r)
    # print(c)
    # print(b)
    print(True)

x = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
isValidSudoku(x)