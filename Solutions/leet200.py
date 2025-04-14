grid = [
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"]
]
def dfs(grid, x, y,num):
    #boundary/visited check
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return 0
    if grid[x][y] != '1':
        return 0
    #visited
    grid[x][y] = -1
    
    dfs(grid, x-1, y,num) #down
    dfs(grid, x+1, y,num) #up
    dfs(grid, x, y-1,num) #left
    dfs(grid, x, y+1,num) #right
    return num+1

def numIslands(grid):
    num=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                num=dfs(grid, i, j,num)
    return num


numIslands(grid)
