class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist_calc(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                wt = dist_calc(points[i], points[j])
                adj[i].append((j, wt))
                adj[j].append((i, wt))

        min_heap = [(0, 0)]
        visit = set()
        
        min_cost = 0
        while min_heap:
            if len(visit) == len(points):
                break
            
            wt, node = heapq.heappop(min_heap)
            if node in visit:
                continue

            min_cost += wt
            visit.add(node)

            for nei,wt in adj[node]:
                if nei not in visit:
                    heapq.heappush(min_heap, (wt, nei))

        return min_cost