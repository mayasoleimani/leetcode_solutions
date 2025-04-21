mat = [[0,0,0],
       [0,1,0],
       [1,1,1]]


from collections import deque

def updateMatrix(mat):
    m = len(mat)
    n = len(mat[0])
    queue = deque()
    visited=set()
    answer =[[0]*n for _ in range(m)] #create list of same size with 0's
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    distance=0

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                queue.append((i, j))
                visited.add((i,j))

    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()
            # if mat[i][j]==1: , unnecessary, as the distance graduates level by level already  
            answer[i][j]=distance
            
            for x in directions:
                new_i=i+x[0]
                new_j=j+x[1]

                if 0 <= new_i < m and 0 <= new_j < n and (new_i,new_j) not in visited:
                    queue.append((new_i,new_j))
                    visited.add((new_i,new_j))
        distance+=1

    return answer
updateMatrix(mat)