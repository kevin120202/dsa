class Solution(object):
    def floodFill(self, image, sr, sc, color):
        if image[sr][sc] == color:
            return image

        og = image[sr][sc]
        height = len(image)
        width = len(image[0])
        def dfs(sr, sc):
            if 0 <= sr and sr < height and 0 <= sc and sc < width and image[sr][sc] == og and image[sr][sc] != color:
                image[sr][sc] = color
                dfs(sr-1,sc)
                dfs(sr+1,sc)
                dfs(sr,sc-1)
                dfs(sr,sc+1)
        
        dfs(sr,sc)

        return image