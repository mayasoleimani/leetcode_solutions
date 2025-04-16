image =[[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

def floodFill(image, sr, sc, color):
    def dfs(image, color, x, y, orig):
        if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != orig:
            return

        image[x][y] = color

        dfs(image, color, x+1, y, orig)
        dfs(image, color, x-1, y, orig)
        dfs(image, color, x, y+1, orig)
        dfs(image, color, x, y-1, orig)

    orig = image[sr][sc]
    if orig == color:
        return image

    dfs(image, color, sr, sc, orig)
    return image


floodFill(image,sr,sc,color)