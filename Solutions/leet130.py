board=[["X","O","X","O","X","O"],
      ["O","X","O","X","O","X"],
      ["X","O","X","O","X","O"],
      ["O","X","O","X","O","X"]]

    
def solve(board):
    
    def dfs(x,y):
        if x < 0 or x >= len(board) or y<0 or y>= len(board[0]) or board[x][y]!="O":
            return 0

        board[x][y]="S"

        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)

    for i in range(len(board)):
        dfs(i,0)
        dfs(i,len(board[0])-1)
    for j in range(len(board[0])):
        dfs(0,j)
        dfs(len(board)-1,j)


    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "S":
                board[i][j] = "O"
            elif board[i][j] =="O":
                board[i][j] = "X"
    return board


solve(board)
