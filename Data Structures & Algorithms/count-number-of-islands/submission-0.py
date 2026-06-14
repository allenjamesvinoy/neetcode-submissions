class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x = len(grid)
        y = len(grid[0])

        visited = [[False for _ in range(y)] for _ in range(x)]

        def dfs(i, j):
            if i>=x or i<0 or j>=y or j<0:
                return 

            if grid[i][j] == "0":
                return

            if visited[i][j]:
                return
            
            visited[i][j] = True
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        islands_count = 0

        for i in range(0,x):
            for j in range(0,y):
                if not visited[i][j] and grid[i][j] == "1":
                    islands_count += 1
                    dfs(i,j)

        return islands_count




            


            
            
            
