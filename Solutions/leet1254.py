grid = [[0,0,1,1,0,1,0,0,1,0],
        [1,1,0,1,1,0,1,1,1,0],
        [1,0,1,1,1,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,0,1],
        [0,0,0,0,0,0,1,1,1,0],
        [0,1,0,1,0,1,0,1,1,1],
        [1,0,1,0,1,1,0,0,0,1],
        [1,1,1,1,1,1,0,0,0,0],
        [1,1,1,0,0,1,0,1,0,1],
        [1,1,1,0,1,1,0,1,1,0]]

def closedIsland(grid):
    def dfs(x,y):
        if x<0 or x>=len(grid) or y<0 or y>= len(grid[0]) or grid[x][y]!=0:
            return 0
        
        grid[x][y]="F" #found

        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
    islands=0
    for i in range(len(grid)):
        dfs(i,0)
        dfs(i,len(grid[0])-1)
    for j in range(len(grid[0])):
        dfs(0,j)
        dfs(len(grid)-1,j)
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                islands+=1
                dfs(i,j)
    return islands

closedIsland(grid)