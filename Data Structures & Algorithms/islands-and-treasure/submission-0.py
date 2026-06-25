class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if grid is None:
            return

        x,y = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        for i in range(0, x):
            for j in range(0, y):
                if grid[i][j] == 0:
                    queue.append((i,j,0))
                    visited.add((i,j))

        co_ord_diff = [(-1,0), (1,0), (0,1), (0,-1)]
        while queue:
            val = queue.popleft()
            for co_ord in co_ord_diff:
                i = val[0] + co_ord[0]
                j = val[1] + co_ord[1]
                if not (i>=0 and i<x and j>=0 and j<y):
                    continue
                
                if (i,j) in visited:
                    continue

                if grid[i][j] == -1:
                    continue

                grid[i][j] = val[2] + 1
                queue.append((i,j,grid[i][j]))
                visited.add((i,j))
