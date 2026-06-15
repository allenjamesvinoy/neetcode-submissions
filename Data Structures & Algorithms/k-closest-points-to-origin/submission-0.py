class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return (x[0]-y[0])**2 + (x[1]-y[1])**2
        
        points_with_dist = []
        for point in points:
            dist_val = dist(point, [0,0])
            points_with_dist.append([dist_val, point[0], point[1]])

        heapq.heapify(points_with_dist)

        res = []
        for i in range(0, k):
            val = heapq.heappop(points_with_dist)
            res.append([val[1], val[2]])

        return res