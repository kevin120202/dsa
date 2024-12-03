from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Defining the rows and cols
        row = len(grid)
        col = len(grid[0])
        # Counter is used to keep track of distinct islands
        counter = 0

        # Traverse the island making sure it checks all the adjacent lands horizontally and vertically and making sure you stay in bounds
        def dfs(i,j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == '0':
                return

            # Marking the visited island so that we don't revisit it    
            grid[i][j] = '0'
            # Traverse through the islands connected
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
        # First find a starting island and start a dfs from there
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    counter += 1
                    dfs(int(i),int(j))


        return counter