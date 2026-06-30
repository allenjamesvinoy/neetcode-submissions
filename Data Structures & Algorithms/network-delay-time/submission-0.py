class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u,v,w in times:
            adj[u].append((v,w))

        min_heap = [(0, k)]
        visit = set()

        res_t = 0

        while min_heap:
            wt, node = heapq.heappop(min_heap)
            if node in visit:
                continue

            visit.add(node)
            res_t = max(res_t, wt)

            for nei, nei_wt in adj[node]:
                heapq.heappush(min_heap, (wt+nei_wt, nei))

        return res_t if len(visit) == n else -1