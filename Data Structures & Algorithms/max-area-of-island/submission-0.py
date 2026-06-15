class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0

        x,y = len(grid), len(grid[0])
        visited = [[False for _ in range(y)] for _ in range(x)]

        max_val = 0

        def dfs(i, j):
            if i>=x or i<0 or j>=y or j<0:
                return 0

            if visited[i][j]:
                return 0
            
            visited[i][j] = True

            if grid[i][j] == 0:
                return 0

            return 1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)

        for i in range(x):
            for j in range(y): 
                if visited[i][j]:
                    continue

                max_val = max(max_val, dfs(i, j))

        return max_val