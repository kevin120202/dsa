class Solution(object):
    def islandPerimeter(self, grid):
        visit = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if i >= rows or j >= cols or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i,j) in visit:
                return 0
            
            visit.add((i,j))
            perim = dfs(i, j+1)
            perim += dfs(i, j-1)
            perim += dfs(i+1, j)
            perim += dfs(i-1, j)

            return perim
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)