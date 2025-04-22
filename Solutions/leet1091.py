from collections import deque
grid = [[0,0,0,0,1],
        [1,0,0,0,0],
        [0,1,0,1,0],
        [0,0,0,1,1],
        [0,0,0,1,0]]


def shortestPathBinaryMatrix(grid):

    m=len(grid)
    n=len(grid[0])
    queue=deque()
    visited=set()
    moves=0
    directions=[(1,1),(-1,-1),(1,0),(0,1),(0,-1),(-1,0),(-1,1),(1,-1)]

    if (grid[0][0] or grid[m-1][n-1])==1:
        return -1
    else:
        queue.append((0,0))
        visited.add((0,0))
    
    while queue:

        for _ in range(len(queue)):
            i,j=queue.popleft()

            if (i,j)==(m-1,n-1):
                return moves+1 

            for _ in directions:
                new_i=i+_[0]
                new_j=j+_[1]

                if 0<=new_i<m and 0<= new_j<n and (new_i,new_j) not in visited and grid[new_i][new_j]!=1:
                    queue.append((new_i,new_j))
                    visited.add((new_i,new_j))
        moves+=1
    return -1
shortestPathBinaryMatrix(grid)