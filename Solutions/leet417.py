heights = [[1,2,2,3,5],
           [3,2,3,4,4],
           [2,4,5,3,1],
           [6,7,1,4,5],
           [5,1,1,2,4]]

def pacificAtlantic(heights):
    rows, cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    def dfs(x, y, visited, prevHeight):
        if (
            x < 0 or x >= rows or
            y < 0 or y >= cols or
            (x, y) in visited or
            heights[x][y] < prevHeight
        ):
            return
        visited.add((x, y))
        dfs(x+1, y, visited, heights[x][y])
        dfs(x-1, y, visited, heights[x][y])
        dfs(x, y+1, visited, heights[x][y])
        dfs(x, y-1, visited, heights[x][y])

    for i in range(cols):
        dfs(0, i, pacific, heights[0][i])
        dfs(rows-1, i, atlantic, heights[rows-1][i])

    for j in range(rows):
        dfs(j, 0, pacific, heights[j][0])
        dfs(j, cols-1, atlantic, heights[j][cols-1])
    #print(pacific & atlantic)
    return list(pacific & atlantic) #intersects both sets, finds common coordinates


pacificAtlantic(heights)