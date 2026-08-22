class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        pacific_queue = deque()
        atlantic_set = set()
        atlantic_queue = deque()

        m = len(heights)
        n = len(heights[0])

        for i in range(m):
            for j in range(n):
                tuple_val = (i,j)
                if i == 0 or j == 0:
                    pacific_set.add(tuple_val)                
                    pacific_queue.append(tuple_val)
                if i == m-1 or j == n-1:
                    atlantic_set.add(tuple_val)
                    atlantic_queue.append(tuple_val)

        neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
        
        while pacific_queue:
            i,j = pacific_queue.popleft()
            val = heights[i][j]
            for nei in neighbors:
                i_hat, j_hat = i+nei[0], j+nei[1]
                if i_hat < 0 or i_hat >= m or j_hat < 0 or j_hat >= n:
                    continue

                cand_val = heights[i_hat][j_hat]
                if cand_val >= val:
                    tuple_val = (i_hat, j_hat)
                    if tuple_val not in pacific_set:
                        pacific_set.add(tuple_val)
                        pacific_queue.append(tuple_val)

        while atlantic_queue:
            i,j = atlantic_queue.popleft()
            val = heights[i][j]
            for nei in neighbors:
                i_hat, j_hat = i+nei[0], j+nei[1]
                if i_hat < 0 or i_hat >= m or j_hat < 0 or j_hat >= n:
                    continue

                cand_val = heights[i_hat][j_hat]
                if cand_val >= val:
                    tuple_val = (i_hat, j_hat)
                    if tuple_val not in atlantic_set:
                        atlantic_set.add(tuple_val)
                        atlantic_queue.append(tuple_val)

        ans_set = pacific_set.intersection(atlantic_set)

        return list(ans_set)


