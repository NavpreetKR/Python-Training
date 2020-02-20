
def queens(board, row, n):
    if row == n:
        print("solution found")
        return
    for col in range(0,n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            queens(board, row + 1, n)
            board[row][col] = False

def is_safe(board, row, col, n):
    max_steps = max(row,col)

    for step in range(1,max_steps+1):
        if row - step >= 0:
            if board[row -step][col]:
                return Falseq
        #lets check left
            if col - step >=0:
                 if board[row-step][col-step]:
                    return False
        #lets check right
            if col + step < n:
                if board[row-step][col+step]:
                     return False
    return True


n = 4
board = [[False] * n for i in range(n)]
queens(board, 0, n)