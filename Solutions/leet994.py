grid = [[0,2]]

from collections import deque
def rottingOranges(grid):

    m=len(grid)
    n=len(grid[0])
    visited=set()
    queue=deque()
    directions=[(1,0),(-1,0),(0,1),(0,-1)]
    minutes=-1
    fresh_check=0


    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i,j))
                visited.add((i,j))
            if grid[i][j] ==1:
                fresh_check+=1
    if fresh_check==0:
        print(0)
        return 0
    
    while queue:
        for _ in range(len(queue)):
            i,j=queue.popleft()
            if grid[i][j]==1:
                grid[i][j]=2

            for _ in directions:
                new_i=i+_[0]
                new_j=j+_[1]
                if 0 <=new_i<m and 0<=new_j<n and (new_i,new_j) not in visited and grid[new_i][new_j]!=0:
                    queue.append((new_i,new_j))
                    visited.add((new_i,new_j))
        minutes+=1
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                print(-1)
                return -1
    print(minutes)
    return minutes

rottingOranges(grid)