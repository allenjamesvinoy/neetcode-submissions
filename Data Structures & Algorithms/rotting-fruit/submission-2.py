class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is None:
            return -1

        queue = deque()
        rows = len(grid)
        cols = len(grid[0])

        fruit_count = 0
        rotten_fruit_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    fruit_count += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
                    rotten_fruit_count += 1

        if fruit_count == rotten_fruit_count:
            return 0

        time = -1
        nei_grid = [[-1, 0], [1,0], [0,1], [0,-1]]
        while queue:
            time += 1

            l = len(queue)
            while l:
                l-=1
                item = queue.popleft()
                for nei in nei_grid:
                    x = nei[0] + item[0]
                    y = nei[1] + item[1]

                    if x >= 0 and x < rows and y >=0 and y < cols:
                        if grid[x][y] == 1:
                            grid[x][y] = 2
                            queue.append((x,y))
                            rotten_fruit_count += 1

        
        rem = False

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rem = True
                    break
            if rem:
                break

        return -1 if rem else time

                
