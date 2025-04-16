grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]

def dfs(grid,x,y):
    if x>=len(grid) or y>=len(grid[0]) or x<0 or y<0:
        return 1
    # is 0 and out of bounds doesnt work
    if grid[x][y]==0:
        return 1
    if grid[x][y] == -1:
        return 0
    
    grid[x][y]=-1

    perimeter=0
    perimeter+=dfs(grid,x+1,y)
    perimeter+=dfs(grid,x-1,y)
    perimeter+=dfs(grid,x,y+1)
    perimeter+=dfs(grid,x,y-1)
    return perimeter

    
def islandPerimeter(grid):

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                return dfs(grid,i,j)

islandPerimeter(grid)