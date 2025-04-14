
def numIslands(grid):
    def dfs(grid, x, y):
        #boundary/visited check
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return 0
        if grid[x][y] != '1':
            return 0
        #visited
        grid[x][y] = -1
        
        dfs(grid, x-1, y) #down
        dfs(grid, x+1, y) #up
        dfs(grid, x, y-1) #left
        dfs(grid, x, y+1) #right

    num=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid,i,j)
                num=+1
    return num
