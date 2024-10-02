class Solution(object):
    def floodFill(self, image, sr, sc, color):
        original_color = image[sr][sc]
        if original_color == color:
            return image

        queue = [(sr, sc)]
        visited = []
        while queue:
            sr, sc = queue.pop(0)
            visited.append((sr, sc))
            image[sr][sc] = color

            neighbors = [(sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)]
            for neighbor in neighbors:
                r, c = neighbor
                if (r >= 0 and r < len(image) and c >= 0 and c < len(image[0]) and (r, c) not in visited
                    and image[r][c] == original_color
                ):
                    queue.append((r, c))
        
        return image

        # original_color = image[sr][sc]
        # if original_color == color:
        #     return image
        
        # def dfs(sr, sc):
        #     if (sr >= 0 and sr < len(image) and sc >= 0 and sc < len(image[0]) and image[sr][sc] == original_color 
        #     and image[sr][sc] != color):
        #         image[sr][sc] = color
        #     else:
        #         return
            
        #     dfs(sr, sc - 1)
        #     dfs(sr, sc + 1)
        #     dfs(sr + 1, sc)
        #     dfs(sr - 1, sc)
        
        # dfs(sr, sc)

        # return image