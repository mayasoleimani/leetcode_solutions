

grid = [[0,0,1,1,0,0,0,1,0,0,0,0,0],
        [0,0,0,1,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]



def maxAreaOfIsland(grid):
    def dfs(grid, x, y):
        #boundary/visited check
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return 0
        if grid[x][y] != 1:
            return 0
        #visited
        grid[x][y] = -1

        area = 1
        area += dfs(grid, x-1, y) #down
        area += dfs(grid, x+1, y) #up
        area += dfs(grid, x, y-1) #left
        area += dfs(grid, x, y+1) #right
        return area
    max_area = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(grid, i, j))
    return max_area


maxAreaOfIsland(grid)
